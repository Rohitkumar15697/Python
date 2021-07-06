#Program of singly linked list


class Node:

    def __init__(self,data):
        self.data=data
        self.next_node=None


class Linkedlist:

    def __init__(self):
        self.head=None

    def printlist(self):

        printval=self.head
        while printval is not None:
            print(printval.data)
           
            printval=printval.next_node

    def adding_node_at_beginning(self,NewData=None):

        NewNode=Node(NewData)

        NewNode.next_node=self.head
        self.head=NewNode
        

    def adding_node_at_end(self,NewData):

        NewNode=Node(NewData)

        last=self.head

        while last.next_node:
            last=last.next_node     #Finding the current last node
        last.next_node=NewNode      #Put newnode after last node
                
        
linkedlist=Linkedlist() 

linkedlist.head=Node(1) #Creating head node with data 1

second=Node(2)          #second node with data value 2

third=Node(3)           #Third node with data value 3

linkedlist.head.next_node=second     #Head's node pointing to the second node

second.next_node=third       #Second node pointing to the third node

#linkedlist.printlist()      #traversing to linked list

linkedlist.adding_node_at_beginning(4)

#linkedlist.printlist()

linkedlist.adding_node_at_end(6)

linkedlist.printlist()
