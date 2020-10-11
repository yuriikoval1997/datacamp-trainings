FROM postgres:latest

COPY ./datasets/countries/. /docker-entrypoint-initdb.d
COPY ./datasets/leaders/. /docker-entrypoint-initdb.d

