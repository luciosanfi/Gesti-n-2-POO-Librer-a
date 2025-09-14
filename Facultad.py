
class Estudiante:
    def __init__(self, nombre, apellido, matricula, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula  # identificador único
        self.carrera = carrera
        self.cursos_inscriptos = []

    def __str__(self):
        cursos = ", ".join([curso.nombre for curso in self.cursos_inscriptos]) or "Ninguno"
        return f"{self.nombre} {self.apellido} (Matrícula: {self.matricula}, Carrera: {self.carrera}) - Cursos: {cursos}"


class Curso:
    def __init__(self, nombre, codigo, profesor, capacidad_maxima):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.capacidad_maxima = capacidad_maxima
        self.estudiantes = []

    def __str__(self):
        return f"{self.nombre} (Código: {self.codigo}, Profesor: {self.profesor}) - Inscritos: {len(self.estudiantes)}/{self.capacidad_maxima}"


class Facultad:
    def __init__(self):
        self.estudiantes = []
        self.cursos = []

    # Registro de estudiantes
    def registrar_estudiante(self, nombre, apellido, matricula, carrera):
        if self.buscar_estudiante(matricula):
            print(f"Ya existe un estudiante con matrícula {matricula}.")
            return
        estudiante = Estudiante(nombre, apellido, matricula, carrera)
        self.estudiantes.append(estudiante)
        print(f"Estudiante registrado: {estudiante.nombre} {estudiante.apellido}")

    # Registro de cursos
    def registrar_curso(self, nombre, codigo, profesor, capacidad_maxima):
        if self.buscar_curso(codigo):
            print(f"Ya existe un curso con código {codigo}.")
            return
        curso = Curso(nombre, codigo, profesor, capacidad_maxima)
        self.cursos.append(curso)
        print(f"Curso registrado: {curso.nombre}")

    # Buscar estudiante por matrícula
    def buscar_estudiante(self, matricula):
        for estudiante in self.estudiantes:
            if estudiante.matricula == matricula:
                return estudiante
        return None

    # Buscar curso por código
    def buscar_curso(self, codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso
        return None

    # Inscripción a curso
    def inscribir_estudiante(self, matricula, codigo):
        estudiante = self.buscar_estudiante(matricula)
        curso = self.buscar_curso(codigo)

        if estudiante and curso:
            if len(curso.estudiantes) < curso.capacidad_maxima:
                if estudiante not in curso.estudiantes:
                    curso.estudiantes.append(estudiante)
                    estudiante.cursos_inscriptos.append(curso)
                    print(f"{estudiante.nombre} se inscribió en {curso.nombre}")
                else:
                    print(f"{estudiante.nombre} ya está inscripto en {curso.nombre}")
            else:
                print(f"No hay cupos disponibles en {curso.nombre}")
        else:
            print("Estudiante o curso no encontrado.")

    # Baja de curso
    def dar_baja_estudiante(self, matricula, codigo):
        estudiante = self.buscar_estudiante(matricula)
        curso = self.buscar_curso(codigo)

        if estudiante and curso:
            if estudiante in curso.estudiantes:
                curso.estudiantes.remove(estudiante)
                estudiante.cursos_inscriptos.remove(curso)
                print(f"{estudiante.nombre} se dio de baja en {curso.nombre}")
            else:
                print(f"{estudiante.nombre} no estaba inscripto en {curso.nombre}")
        else:
            print("Estudiante o curso no encontrado.")

    # Consulta de cursos
    def mostrar_cursos(self):
        print("\nEstado de los cursos:")
        for curso in self.cursos:
            inscritos = ", ".join([f"{e.nombre} {e.apellido}" for e in curso.estudiantes]) or "Ninguno"
            print(f"{curso} - Estudiantes: {inscritos}")

    # Consulta de estudiantes
    def mostrar_estudiantes(self):
        print("\nEstado de los estudiantes:")
        for estudiante in self.estudiantes:
            print(estudiante)

# Simulación del sistema
if __name__ == "__main__":
    facultad = Facultad()

    # Registro de estudiantes
    facultad.registrar_estudiante("Lucio", "Sanfilippo", "E001", "Sistemas")
    facultad.registrar_estudiante("Ana", "García", "E002", "Derecho")

    # Registro de cursos
    facultad.registrar_curso("Programación", "C101", "Prof. López", 2)
    facultad.registrar_curso("Derecho Civil", "C102", "Prof. Pérez", 1)

    # Inscripción
    facultad.inscribir_estudiante("E001", "C101")
    facultad.inscribir_estudiante("E002", "C101")
    facultad.inscribir_estudiante("E002", "C102")  # este último queda lleno

    # Consultas
    facultad.mostrar_cursos()
    facultad.mostrar_estudiantes()

    # Baja
    facultad.dar_baja_estudiante("E001", "C101")
    facultad.mostrar_cursos()
    facultad.mostrar_estudiantes()
