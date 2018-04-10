drop table if exists grids;
create table grids (
    id integer primary key autoincrement,
    grid_id text not null,
    data text not null,
    x1 float not null,
    x2 float not null,
    y1 float not null,
    y3 float not null
);

drop table if exists adresses;
create table adresses (
    id integer primary key autoincrement,
    housenr integer not null,
    street_name text not null,
    adress_ext text,
    lon float not null,
    lat float not null
);

drop table if exists streets;
create table streets (
    id integer primary key autoincrement,
    street_name text not null,
    lon float not null,
    lat float not null
);

.mode csv
.import data/grids.csv grids
.import data/streets.csv streets
.import data/adresses.csv adresses
