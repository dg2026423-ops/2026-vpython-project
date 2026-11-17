Web VPython 3.2

background = box(texture = "https://static.wikia.nocookie.net/splatoon/images/4/46/S3_promo_screenshot_story_Alterna_00.jpg/revision/latest/top-crop/width/360/height/450?cb=20211002215941",size=vec(7,9,0.5),pos=vec(-8,0,0))
     

b = box(texture = "https://static.wikia.nocookie.net/splatoon/images/b/b8/Smallfry-LittleBuddy.png/revision/latest?cb=20230625062414",pos = vec(8,-4,0))
#if abs(a.pos.x - b.pos.x) < 1 :
#    a.color = color.red
while True :
    rate(100)
    k = keysdown()
    if 'w' in k :
        for i in range(20):
            b.pos.y = b.pos.y + 0.1
            rate(100)
#        rate(100)
        for i in range(20):
            b.pos.y = b.pos.y - 0.1
            rate(100)
        
    if 'a' in k :
        b.pos.x = b.pos.x - 0.1 
                
#    if 's' in k : 
#        b.pos.y = b.pos.y - 0.1 
        
    if 'd' in k : 
        b.pos.x = b.pos.x + 0.1   

    if b.pos.x <= -4:
        print('')
        print('')
        print('★★CLEAR★★')
        print('')

if 'b = box(texture = "https://static.wikia.nocookie.net/splatoon/images/b/b8/Smallfry-LittleBuddy.png/revision/latest?cb=20230625062414",pos = vec(8,-4,0))' in background :                                                                                                                                             
        b.print('clear')
        
# -4
# -5
# -12
# 5
        
        
    
   
        
  

     






    




    

             
   
