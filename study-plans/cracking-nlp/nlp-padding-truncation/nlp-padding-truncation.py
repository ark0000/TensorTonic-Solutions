def pad_and_truncate(sequences, max_length, pad_value=0):
    t=[]
    for i in sequences:
        if(len(i)<max_length):
            times=max_length-len(i)
            
            for _ in range(0,times):
                
                i.append(pad_value)
            t.append(i)
        else:
          t.append(i[:max_length])
                
    return t            
    
    """
    Returns: list[list[int]]
    """
    pass