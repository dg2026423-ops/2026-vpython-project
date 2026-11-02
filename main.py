b = box(texture = "https://static.wikia.nocookie.net/splatoon/images/b/b8/Smallfry-LittleBuddy.png/revision/latest?cb=20230625062414")
while True :
    rate(100)
    k = keysdown()
    if 'w' in k :
        b.pos.y = b.pos.y + 0.1 
        
    if 'a' in k :
        b.pos.x = b.pos.x - 0.1 
                
    if 's' in k : 
        b.pos.y = b.pos.y - 0.1 
        
    if 'd' in k : 
        b.pos.x = b.pos.x + 0.1   
        
   
