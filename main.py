
class Person:
    def greet(self) -> None:
        raise NotImplementedError("You have not implemented this function.")
    
# kevin 向廷
class Kevin(Person):
    def greet(self) -> None:
        print("Hello, my name is 向廷")

# river 俊穎

# smith 君偉
class Smith(Person):
    def greet(self) -> None:
        print("Hello, my name is 君偉")
# david 昕哲

if __name__ == "__main__":

    # kevin 向廷
    Kevin().greet()

    # river 俊穎

    # smith 君偉
    Smith().greet()

    # david 昕哲

    print("hello world")
