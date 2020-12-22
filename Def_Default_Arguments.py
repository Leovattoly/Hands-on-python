def ask_ok(prompt,retries=0,reminde='Please Try Again Later'):
    while True:
        #ok=input(prompt)
        ok=prompt
        if ok in ('Y','y','Yeah','yes','Yes'):
            #print ("U meant yes")
            return  True
        if ok in ('n','N','no','Nope'):
            #print ("U meant NO")
            return False
        retries= retries-1
        if retries<0:
            raise ValueError('Invalid user response')
        print (reminde)

repaly=input("Please enter your response:")
ask_ok(repaly)
