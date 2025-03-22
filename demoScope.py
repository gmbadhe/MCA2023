def fun1(): # outer function
    msg = "PES MIBS PUNE"
    
    def fun2(): # inner function
        print(msg)  # accessing outer function's variable
    
    fun2()
fun1()
