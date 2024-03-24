import sqlite3
from datetime import datetime

# Función para conectar a la base de datos
def connect_db():
    con = sqlite3.connect("school.db")
    return con

# Función para cerrar la conexión a la base de datos
def close_db(con):
    con.close()

# Función para crear un nuevo usuario
def create_user():
    con = connect_db()
    cursor = con.cursor()

    email = input("Ingrese el email del usuario: ")
    password = input("Ingrese la contraseña: ")
    status = input("Ingrese el estado (1 para activo, 0 para inactivo): ")

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO users (email, password, status, created_at) VALUES (?, ?, ?, ?)",
                   (email, password, status, created_at))
    
    con.commit()
    close_db(con)
    print("Usuario creado exitosamente.")

# Función para crear un nuevo tipo de identificación
def create_identification_type():
    con = connect_db()
    cursor = con.cursor()

    name = input("Ingrese el nombre del tipo de identificación: ")
    abrev = input("Ingrese la abreviatura: ")
    descrip = input("Ingrese la descripción: ")

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO identification_types (name, abrev, descrip, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                   (name, abrev, descrip, created_at, created_at))
    
    con.commit()
    close_db(con)
    print("Tipo de identificación creado exitosamente.")

# Función para crear una nueva persona
def create_person():
    con = connect_db()
    cursor = con.cursor()

    first_name = input("Ingrese el nombre de la persona: ")
    last_name = input("Ingrese el apellido: ")
    id_ident_type = input("Ingrese el ID del tipo de identificación: ")
    ident_number = input("Ingrese el número de identificación: ")
    id_exp_city = input("Ingrese el ID de la ciudad de expedición: ")
    id_user = input("Ingrese el ID del usuario asociado (opcional, presione Enter si no hay): ")
    address = input("Ingrese la dirección: ")
    mobile = input("Ingrese el número de teléfono móvil: ")

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO persons (first_name, last_name, id_ident_type, ident_number, id_exp_city, "
                   "id_user, address, mobile, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (first_name, last_name, id_ident_type, ident_number, id_exp_city, id_user, address, mobile, created_at, created_at))
    
    con.commit()
    close_db(con)
    print("Persona creada exitosamente.")


# Función para crear un nuevo estudiante
def create_student():
    con = connect_db()
    cursor = con.cursor()

    code = input("Ingrese el código del estudiante: ")
    id_person = input("Ingrese el ID de la persona asociada: ")
    status = input("Ingrese el estado del estudiante (1 para activo, 0 para inactivo): ")

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO students (code, id_person, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
                   (code, id_person, status, created_at, created_at))
    
    con.commit()
    close_db(con)
    print("Estudiante creado exitosamente.")


# Función para crear una nueva ciudad
def create_city():
    con = connect_db()
    cursor = con.cursor()

    name = input("Ingrese el nombre de la ciudad: ")
    abrev = input("Ingrese la abreviatura: ")
    descrip = input("Ingrese la descripción: ")
    id_dept = input("Ingrese el ID del departamento asociado: ")

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO cities (name, abrev, descrip, id_dept, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, abrev, descrip, id_dept, created_at, created_at))
    
    con.commit()
    close_db(con)
    print("Ciudad creada exitosamente.")


# Función para crear un nuevo departamento
def create_department():
    con = connect_db()
    cursor = con.cursor()

    name = input("Ingrese el nombre del departamento: ")
    abrev = input("Ingrese la abreviatura: ")
    descrip = input("Ingrese la descripción: ")
    id_country = input("Ingrese el ID del país asociado: ")

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO departments (name, abrev, descrip, id_country, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, abrev, descrip, id_country, created_at, created_at))
    
    con.commit()
    close_db(con)
    print("Departamento creado exitosamente.")


# Función para crear un nuevo país
def create_country():
    con = connect_db()
    cursor = con.cursor()

    name = input("Ingrese el nombre del país: ")
    descrip = input("Ingrese la descripción: ")

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO countries (name, descrip, created_at, updated_at) VALUES (?, ?, ?, ?)",
                   (name, descrip, created_at, created_at))
    
    con.commit()
    close_db(con)
    print("País creado exitosamente.")

# Menú principal
def main_menu():
    while True:
        print("\nMain Menu")
        print("[1] Crear usuario")
        print("[2] Crear estudiante")
        print("[3] Crear tipo de identificación")
        print("[4] Crear persona")
        print("[5] Crear ciudad")
        print("[6] Crear departamento")
        print("[7] Crear país")
        print("[0] Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            create_student()
        elif choice == "3":
            create_identification_type()
        elif choice == "4":
            create_person()
        elif choice == "5":
            create_city()
        elif choice == "6":
            create_department()
        elif choice == "7":
            create_country()
        elif choice == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main_menu()
