# Sistema de Gestión de Biblioteca con POO en Python

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        self.prestado_a = None

    def __str__(self):
        estado = "Disponible" if self.disponible else f"Prestado a {self.prestado_a.nombre}"
        return f"[{self.isbn}] {self.titulo} - {self.autor} ({estado})"


class Miembro:
    def __init__(self, nombre, miembro_id):
        self.nombre = nombre
        self.miembro_id = miembro_id
        self.libros_prestados = []

    def __str__(self):
        libros = ", ".join([libro.titulo for libro in self.libros_prestados]) or "Ninguno"
        return f"{self.nombre} (ID: {self.miembro_id}) - Libros prestados: {libros}"


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []

    # Registro de libros
    def registrar_libro(self, titulo, autor, isbn):
        libro = Libro(titulo, autor, isbn)
        self.libros.append(libro)
        print(f"Libro registrado: {libro.titulo}")

    # Registro de miembros
    def registrar_miembro(self, nombre, miembro_id):
        miembro = Miembro(nombre, miembro_id)
        self.miembros.append(miembro)
        print(f"Miembro registrado: {miembro.nombre}")

    # Buscar libro por ISBN
    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    # Buscar miembro por ID
    def buscar_miembro(self, miembro_id):
        for miembro in self.miembros:
            if miembro.miembro_id == miembro_id:
                return miembro
        return None

    # Préstamo de libros
    def prestar_libro(self, isbn, miembro_id):
        libro = self.buscar_libro(isbn)
        miembro = self.buscar_miembro(miembro_id)

        if libro and miembro:
            if libro.disponible:
                libro.disponible = False
                libro.prestado_a = miembro
                miembro.libros_prestados.append(libro)
                print(f"{miembro.nombre} ha tomado prestado '{libro.titulo}'")
            else:
                print(f"El libro '{libro.titulo}' no está disponible.")
        else:
            print("Libro o miembro no encontrado.")

    # Devolución de libros
    def devolver_libro(self, isbn, miembro_id):
        libro = self.buscar_libro(isbn)
        miembro = self.buscar_miembro(miembro_id)

        if libro and miembro:
            if libro in miembro.libros_prestados:
                libro.disponible = True
                libro.prestado_a = None
                miembro.libros_prestados.remove(libro)
                print(f"{miembro.nombre} devolvió '{libro.titulo}'")
            else:
                print(f"{miembro.nombre} no tiene prestado '{libro.titulo}'")
        else:
            print("Libro o miembro no encontrado.")

    # Consulta de libros
    def mostrar_libros(self):
        print("\nEstado de los libros:")
        for libro in self.libros:
            print(libro)

    # Consulta de miembros
    def mostrar_miembros(self):
        print("\nEstado de los miembros:")
        for miembro in self.miembros:
            print(miembro)



# simulación de uso del sistema
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Registro de libros
    biblioteca.registrar_libro("Cien años de soledad", "Gabriel García Márquez", "111")
    biblioteca.registrar_libro("El pasado", "Alan Pauls", "978-84-339-6852-4")

    # Registro de miembros
    biblioteca.registrar_miembro("Lucio", "M1")
    biblioteca.registrar_miembro("Ana", "M2")

    # Préstamo de libros
    biblioteca.prestar_libro("111", "M1")

    # Consultas
    biblioteca.mostrar_libros()
    biblioteca.mostrar_miembros()

    # Devolución
    biblioteca.devolver_libro("111", "M1")
    biblioteca.mostrar_libros()
    biblioteca.mostrar_miembros()
