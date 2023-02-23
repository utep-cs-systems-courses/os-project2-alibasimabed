import os, sys, time, re


print("Hello, Welcome to Ali's Shell. I hope you have fun. Report any issues to aaljanabi@miners.utep.edu")
while True:
    time.sleep(5)
    args = [str(x) for x in input(">>>>>>> ").split(' ')]
    if args[0] == 'quit':
        break

    pid = os.getpid()             
    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:
        #args = ["wc", "README.md"]
        #args = sys.argv[1:]
        #os.write(2,("here  %s\n" %args).encode())
        
        
        #os.close(1)            
        #sys.stdout = open("output.txt", "w")
        #os.set_inheritable(1, True)


        for dir in re.split(":", os.environ['PATH']): # try each directory in path
            program = "%s/%s" % (dir, args[0])
            try:
                os.execv(program, args) 
                #print()
            except FileNotFoundError:             
                pass                 
            

        os.write(2, ("Child:    Error: Could not exec %s\n" % args[0]).encode())
        sys.exit(1)         


