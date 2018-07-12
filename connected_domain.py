def connected_domain(img,size,threshold):
    '''
    img: the input 
    size: 4 or 8
    threshold: domian that is less than the threshold will be deleted 
    
    '''
    
    assert isinstance(size,int)
    assert size in (4,8),print("only has two type size  4 or 8")
    assert len(img.shape)
    print(img.shape)
    h,w=img.shape
    color_type=[(255,255,255),(255,0,0),(0,0,255),(0,255,0),(255,0,255),(255,255,0),(0,255,255)]
    color=np.zeros([h,w,3])
    direction_8=[(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1)]
    direction_4=[(0,1),(-1,0),(0,-1),(1,0)]
    count_total=[]
    if size==4:
        label_num=0
        visit_queue=queue.LifoQueue()
        label=np.zeros(img.shape,dtype=np.int)
        for i in np.arange(1,h-1):
            for j in np.arange(1,w-1):
                if img[i,j]==0 and label[i,j]==0:
                    count=1
                    label_num+=1
                    label[i,j]=label_num
                    for pair in direction_4:
                        if img[i+pair[0],j+pair[1]]==0 and label[i+pair[0],j+pair[1]]==0:
                            count+=1
                            visit_queue.put((i+pair[0],j+pair[1]))
                            label[i+pair[0],j+pair[1]]=label_num
                    while not visit_queue.empty():
                        i_t,j_t=visit_queue.get()
                        for pair in direction_4:
                            if i_t+pair[0]<h and j_t+pair[1]<w:
                                if label[i_t+pair[0],j_t+pair[1]]==0 and img[i_t+pair[0],j_t+pair[1]]==0:
                                    count+=1
                                    label[i_t+pair[0],j_t+pair[1]]=label_num
                                    visit_queue.put((i_t+pair[0],j_t+pair[1]))
                    count_total.append(count)

    else :
        label_num = 0
        visit_queue = queue.LifoQueue()
        label = np.zeros(img.shape, dtype=np.int)
        for i in np.arange(1, h - 1):
            for j in np.arange(1, w - 1):
                if img[i, j] == 0 and label[i, j] == 0:
                    count=1
                    label_num += 1
                    label[i, j] = label_num
                    for pair in direction_8:
                        if img[i + pair[0], j + pair[1]] == 0 and label[i+pair[0],j+pair[1]]==0:
                            visit_queue.put((i + pair[0], j + pair[1]))
                            label[i + pair[0], j + pair[1]] = label_num
                            count+=1
                    while not visit_queue.empty():
                        i_t, j_t = visit_queue.get()
                        for pair in direction_8:
                            if label[i_t + pair[0], j_t + pair[1]] == 0 and img[i_t + pair[0], j_t + pair[1]] == 0:
                                label[i_t + pair[0], j_t + pair[1]] = label_num
                                visit_queue.put((i_t + pair[0], j_t + pair[1]))
                                count+=1
                    count_total.append(count)
    To_be_deleted=list(np.where(np.array(count_total)<threshold)[0]+1)
    for i in range(h):
        for j in range(w):
            if label[i,j] in To_be_deleted:
                img[i,j]=255
    # for i in range(h):
    #     for j in range(w):
    #         color[i,j]=color_type[label[i,j]%7]
    return img
