CREATE TABLE stars (
    movie_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(person_id) REFERENCES people(id)
);
CREATE TABLE directors (
    movie_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(person_id) REFERENCES people(id)
);
CREATE TABLE ratings (
    movie_id INTEGER NOT NULL,
    rating REAL NOT NULL,
    votes INTEGER NOT NULL,
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);
CREATE TABLE people (
    id INTEGER,
    name TEXT NOT NULL,
    birth NUMERIC,
    PRIMARY KEY(id)
);
CREATE TABLE movies_new (
    id VARCHAR(20),
    title TEXT NOT NULL,
    year NUMAERIC,
    PRIMARY KEY(id)
);
CREATE TABLE people_new (
    id VARCHAR(20),
    name TEXT NOT NULL,
    birth NUMERIC,
    PRIMARY KEY(id)
);
CREATE TABLE stars_new (
    movie_id VARCHAR(20) NOT NULL,
    person_id VARCHAR(20) NOT NULL,
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(person_id) REFERENCES people(id)
);
CREATE TABLE edges(
    from_id VARCHAR(20),
    to_id VARCHAR(20)
);
