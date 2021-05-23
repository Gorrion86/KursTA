class MyFc():
    var1 = 1
    var2 = 2
    def function(self):
        print('Hell')
object = MyFc()
object.var1
object2 = MyFc()
object2.var2

print(object.var1)
print(object2.var2)

object3 = MyFc()
object3.function()