from database.db import get_connection
from .entities.movie import Movie

class MovieModel():
    @classmethod
    def get_movies(self):
        try: 
            connection=get_connection()
            movies=[]
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, title, duration, released FROM movies ORDER BY title ASC")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    movie=Movie(row[0],row[1],row[2],row[3])
                    movies.append(movie.to_JSON())
                    
            connection.close()
            return movies
        except Exception as ex:
            raise Exception(ex)
    
    #Obtener el id de la pelicula
    @classmethod
    def get_movie(self,id):
        try: 
            connection=get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, title, duration, released FROM movies WHERE id=%s", (id,))
                row=cursor.fetchone()
                
                movie=None
                if row != None:
                    movie=Movie(row[0],row[1],row[2],row[3])
                    movie=movie.to_JSON()
                    
            connection.close()
            return movie
        except Exception as ex:
            raise Exception(ex)
    
    #Agregar pelis
    @classmethod
    def add_movie(self,movie):
        try: 
            connection=get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO movies (id, title, duration, released)
                               VALUES (%s,%s,%s,%s)""", (movie.id, movie.title, movie.duration, movie.released))
                affected_rows=cursor.rowcount
                connection.commit()
                    
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    #Update pelis
    @classmethod
    def update_movie(self,movie):
        try: 
            connection=get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE movies SET title = %s, duration=%s, released=%s
                               WHERE id=%s""", (movie.title, movie.duration, movie.released, movie.id))
                affected_rows=cursor.rowcount
                connection.commit()
                    
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    #Eliminar pelis
    @classmethod
    def delete_movie(self,movie):
        try: 
            connection=get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM movies WHERE id=%s", (movie.id))
                affected_rows=cursor.rowcount
                connection.commit()
                    
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)