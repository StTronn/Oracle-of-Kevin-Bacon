from collections import deque
import sqlite3
import sys 

conn =sqlite3.connect("movies.db",check_same_thread=False)
cur=conn.cursor()

class Movie():
    def __init__(self,id,cur):
        self.cur=cur
        self.id=id
        self.name=self.get_name()
        self.year=self.get_year()

    def get_name(self):
        return self.cur.execute("SELECT title FROM movies_new WHERE id=?",(self.id,)).fetchone()[0]
    def get_year(self):
        return self.cur.execute("SELECT year FROM movies_new WHERE id=?",(self.id,)).fetchone()[0]
    def get_attr(self):
        return {"type":"movie","name":self.name,"year":self.year,"id":self.id}

class Star():
    def __init__(self,id,cur):
        self.cur=cur
        self.id=id
        self.name=self.get_name()
        self.year=self.get_year()

    def get_name(self):
        return self.cur.execute("SELECT name FROM people_new WHERE id=?",(self.id,)).fetchone()[0]

    def get_year(self):
        return self.cur.execute("SELECT birth FROM people_new WHERE id=?",(self.id,)).fetchone()[0]
                 
    def get_attr(self):
        return {"type":"actor","name":self.name,"year":self.year,"id":self.id}

class Node():
    def __init__(self,id,cur):
        self.cur=cur
        self.obj=self.get_obj(id)
    def get_obj(self,id):
        if id[:2]=="mv":   
            return Movie(id,self.cur)
        if id[:1]=="p":
            return Star(id,self.cur)

    def get_attr(self):
        return self.obj.get_attr()
    


def get_id(name):
    cur.execute("SELECT id FROM people_new WHERE name=?",(name,))
    ret=cur.fetchone()
    if ret!=None:
        return ret[0]
    else:
        #add exception handling 
        return None    

def bfs(start,end):
    visited={}
    parent={}
    q=deque()

    q.append(start)
    parent[start]=None
    visited[start]=1

    while q:
        nodes_on_this_level=[]
        edges={}
        while q:
            nodes_on_this_level.append(q.popleft())

        query=f"SELECT from_id,to_id FROM edges WHERE from_id IN ({','.join(['?']*len(nodes_on_this_level))})"
        for (from_id,to_id) in conn.execute(query,nodes_on_this_level):
            if from_id not in edges:
                edges[from_id]=[]
            edges[from_id].append(to_id)
        for node in nodes_on_this_level:
            for id in edges[node]:
                if id not in visited:
                    visited[id]=1
                    q.append(id)
                    parent[id]=node
                    if(id==end): return parent 
def get_path(actor_name):
    end=get_id(actor_name)
    ret=[]
    if end==None:
        return ret
    parent=bfs("p102",end)
    x=end
    while x!=None:
        ret.append(Node(x,cur).get_attr())
        x=parent[x]
    return ret

if __name__ == "__main__":
    if len(sys.argv)==1:
        print ("please specify the actor name")
    s=""
    for word in sys.argv[1:]:
        s+=" "+word
    s=s[1:]
    print(get_path(s))
    
# parent=bfs("p102","p1191")

# x="p1191"
# while x!=None:
#     print(Node(x,cur).get_attr())
#     x=parent[x]

# frontier=("p102","mv4519562")
# s=""
# query=f"SELECT to_id FROM edges WHERE from_id IN ({','.join(['?']*len(frontier))})"
# for item in conn.execute(query,frontier):
      


##print(Node("p102",cur).get_attr())
# parent=bfs("p102","p5212")
# x="p375"
# while x!=None:
#     print(Node(x,cur).get_attr())
#     x=parent[x]
