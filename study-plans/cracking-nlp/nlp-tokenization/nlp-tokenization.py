def tokenize(text):
    li=[]
    temp=[]
    for i in text:
      
      if(i.isalnum() or i=="_"):
        li.append(i)
      else:
          if li:
            temp.append("".join(li))
          li=[]
          if i!=" ":
           temp.append(i)
    if li :  
      temp.append("".join(li))
    return temp    
    
    """
    Returns: list[str]
    """
    pass