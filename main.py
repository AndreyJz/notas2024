import modulos.gestoralumnos as st
import modulos.menu as m
if __name__ == '__main__':
    alumnos = {}
    AppRuning = True
    while AppRuning:
        op=m.menu()
        if (op==1):
            isAddStudent = True
            while isAddStudent:
                st.os.system('cls')
                st.AddStudent(alumnos)
                isAddStudent = bool(input('Desea seguir agregando estudiantes? S(si) o Enter(no) '))
        if (op==2):
            isSearching = True
            while isSearching:
                st.os.system('cls')
                st.SearchStudent(alumnos)
                isSearching = bool(input('Desea seguir buscando? S(si) o Enter(no) '))
        if (op==3):
            isList = True
            while isList:
                st.os.system('cls')
                st.ListData(alumnos)
                isList = bool(input('Desea seguir mirando la lista? S(si) o Enter(no) '))
        if (op==4):
            isAddGrades = True
            while isAddGrades:
                st.os.system('cls')
                opG=m.menuGrades()
                if (opG==1):
                    isAddParciales = True
                    while isAddParciales:
                        st.os.system('cls')
                        st.agregarParcial(alumnos)
                        isAddParciales = bool(input('Desea seguir agregando parciales? S(si) o Enter(no) '))
                if (opG==2):
                    isAddQuizes = True
                    while isAddQuizes:
                       st.os.system('cls')
                       st.agregarQuizes(alumnos)
                       isAddQuizes = bool(input('Desea seguir agregando quizes? S(si) o Enter(no) ')) 
                if (opG==3):
                    isAddTrabajos = True
                    while isAddTrabajos:
                        st.os.system('cls')
                        st.agregarTrabajos(alumnos)
                        isAddTrabajos = bool(input('Desea seguir agregando trabajos? S(si) o Enter(no) '))
                if (opG==4):
                    isAddGrades=False
                isAddGrades = bool(input('Desea seguir agregando notas? S(si) o Enter(no) '))
        if (op==5):
            isDelStudent = True
            while isDelStudent:
                st.os.system('cls')
                st.DelStudent(alumnos)
                isDelStudent = bool(input('Desea seguir eliminando estudiantes? S(si) o Enter(no) '))
        if (op==6):
            st.os.system('cls')
            AppRuning = False
    
    print('''
          ___________________________________
          |Gracias por usar este programa c:|
          -----------------------------------
          ''')
    st.os.system('pause')
        


