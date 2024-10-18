class Email:
    existing_emails = []
    def __init__(self, email) -> None:
        if email not in Email.existing_emails:
            self.email = email
            self.inbox = []
            self.sent = []
            Email.existing_emails.append(email)
        else:
            print('your email is existed, pleas choose another!')
    def send(self,other, message):
        self.sent.append(message)
        other.inbox.append(message)
    def read(self):
        print(self.inbox)


    # Stack
class Stack:
    def __init__(self):
        self.__stack = []
    def push(self,item):
        return self.__stack.append(item)
    def peek(self):
        if self.__stack:
            return self.__stack[-1]
        else:
            return "the stack is empty"
    def pop(self):
        if self.__stack:
            return self.__stack.pop()
        else:
            return "the stack is empty"
    def is_empty(self):
        return not bool(self.__stack)
    def size(self):
        return len(self.__stack)
    

#Queue
class Queue:
    def __init__(self):
        self.__queue = []
    def enqueue(self, item):
        return self.__queue.insert(0,item)
    def dequeue(self):
        if self.is_empty():
            return 'the queue is empty'
        else: 
            return self.__queue.pop()
    def front(self):
        return self.__queue[-1]
    def size(self):
        return len(self.__queue) 
    def is_empty(self):
        return not bool(self.__queue)
    def __str__(self):
        return str(self.__queue)
    def __repr__(self) -> str:
        return str(self.__queue) 
    
print("My_classes is imported")