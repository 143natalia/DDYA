class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def newNode():
    temp = node(-1)
    temp.left = None
    temp.right = None
    return(temp);

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    def isValid(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        if node.data <= lower or node.data >= upper:
            return False
        return isValid(node.left, lower, node.data) and isValid(node.right, node.data, upper)
    return isValid(root)
ht = int(input())
cnt = 0
values = map(int, input().split(' '))
values = list(values)
root  = newNode()
def inorder(root, ht):
    global cnt
    global values
    if cnt == len(values):
        return
    else:
        if(ht>0):
            root.left = newNode();
            inorder(root.left, ht-1);
        root.data = values[cnt];
        cnt+=1
        if(ht>0):
            root.right = newNode();
            inorder(root.right, ht-1);
inorder(root, ht);
if(check_binary_search_tree_(root)):
    print("Yes")
else:
    print("No")