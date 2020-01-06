# Oracle of Bacon 

Find a link between Actor A and Kevin Bacon

inspired [from following site](https://oracleofbacon.org/) and  [paper](https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch20.pdf)

The db and script uses a breadth-first search (BFS) to find the shortest path between pairs of actors

## Usage

The link can be find using python cli or site

For python run `queries.py` with actor name which returns a list of actors and movies forming the link.

`python3 queries.py <Actor Name>`

```
python3 queries.py Robert Downey Jr.

[{'type': 'actor', 'name': 'Robert Downey Jr.', 'year': 1965, 'id': 'p375'}, {'type': 'movie', 'name': 'Iron Man 2', 'year': 2010, 'id': 'mv1228705'}, {'type': 'actor', 'name': 'Mickey Rourke', 'year': 1952, 'id': 'p620'}, {'type': 'movie', 'name': 'Diner', 'year': 1982, 'id': 'mv83833'}, {'type': 'actor', 'name': 'Kevin Bacon', 'year': 1958, 'id': 'p102'}]
```

You could also simply open index.html on your browser while running the flask server and type the actor name to get path.

## install

1. clone the repository
2. download movies.db from imdb
3. run universal.py and edges.py to represent a graph
4. install flask 
