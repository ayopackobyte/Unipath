from modelos import Asignatura
from grafo import Grafo


class Gestor:

    def __init__(self):
        self.carreras = {}
        self.facultades = {}

        self.carrera_actual = ""
        self.materias = {}
        self.grafo = Grafo()
        self.aprobadas = []

        self.cargar_datos_iniciales()

    def cargar_datos_iniciales(self):

        materias_sistemas = {}
        grafo_sistemas = Grafo()

        lista_sistemas = [
        Asignatura("PIU101", "Proyección e integración universitaria", 3, 1),
        Asignatura("CYL101", "Comunicación y lenguaje I", 3, 1),
        Asignatura("ITIC101", "Introducción a las TIC", 3, 1),
        Asignatura("A1CE101", "A1 Communicative English", 3, 1),
        Asignatura("MB101", "Matemática básica", 4, 1),
        Asignatura("IP101", "Introducción a la programación", 4, 1),
        Asignatura("INOP101", "Identidad nacional y orgullo patrio", 3, 1),
        Asignatura("EAF101", "Electiva actividades de facultad", 3, 1),
        Asignatura("ADS201", "Análisis y diseño de sistemas", 4, 2),
        Asignatura("PE201", "Programación estructurada", 4, 2),
        Asignatura("C201", "Cálculo I", 4, 2),
        Asignatura("A2CE201", "A2 Communicative English", 3, 2),
        Asignatura("PCD201", "Plataformas de colaboración digital", 3, 2),
        Asignatura("CYL201", "Comunicación y lenguaje II", 3, 2),
        Asignatura("FR201", "Fundamentos de robótica", 4, 2),
        Asignatura("HIN201", "Historia e identidad nacional", 3, 2),
        Asignatura("BD301", "Base de datos I", 4, 3),
        Asignatura("MDI301", "Metodología de la investigación", 3, 3),
        Asignatura("A2PCE301", "A2+ Communicative English", 3, 3),
        Asignatura("CII301", "Cálculo II", 4, 3),
        Asignatura("E301", "Estadística I", 4, 3),
        Asignatura("POO301", "Programación orientada a objetos", 4, 3),
        Asignatura("TDR301", "Tecnología de redes I", 4, 3),
        Asignatura("AL401", "Álgebra lineal", 4, 4),
        Asignatura("TDRII401", "Tecnología de redes II", 4, 4),
        Asignatura("PAD401", "Programación de aplicaciones de escritorio", 4, 4),
        Asignatura("ADB401", "Administración de bases de datos", 4, 4),
        Asignatura("B1CE401", "B1 Communicative English", 3, 4),
        Asignatura("EA401", "Educación ambiental", 3, 4),
        Asignatura("FA501", "Física aplicada", 4, 5),
        Asignatura("B1PCE501", "B1+ Communicative English", 3, 5),
        Asignatura("DAM501", "Desarrollo de aplicaciones móviles I", 4, 5),
        Asignatura("DWF501", "Desarrollo web frontend", 4, 5),
        Asignatura("DAMI501", "Desarrollo de aplicaciones multimedia I", 4, 5),
        Asignatura("ADS501", "Administración de servidores", 4, 5),
        Asignatura("IS501", "Ingeniería de software I", 4, 5),
        Asignatura("DAMII601", "Desarrollo de aplicaciones móviles II", 4, 6),
        Asignatura("DAMMII601", "Desarrollo de aplicaciones multimedia II", 4, 6),
        Asignatura("ISII601", "Ingeniería de software II", 4, 6),
        Asignatura("B2CE601", "B2 Communicative English", 3, 6),
        Asignatura("DWB601", "Desarrollo web backend", 4, 6),
        Asignatura("POI701", "Planificación y organización informática", 4, 7),
        Asignatura("FIA701", "Fundamentos de inteligencia artificial", 4, 7),
        Asignatura("SLI701", "Seguridad y legislación informática", 4, 7),
        Asignatura("ITP701", "Integración de tecnologías y plataformas", 4, 7),
        Asignatura("SD701", "Sistemas distribuidos", 4, 7),
        Asignatura("ML801", "Machine Learning", 4, 8),
        Asignatura("NE801", "Negocio electrónico", 3, 8),
        Asignatura("AI801", "Auditoría informática", 4, 8),
        Asignatura("SII801", "Soluciones de inteligencia de negocios", 4, 8),
        Asignatura("GSTI801", "Gestión de servicios de TI", 4, 8),
        Asignatura("RN901", "Redes neuronales", 4, 9),
        Asignatura("GPT901", "Gestión de proyectos tecnológicos", 4, 9),
        Asignatura("PPI901", "Prácticas profesionales I", 4, 9),
        Asignatura("IPN901", "Ingeniería de procesos de negocio", 4, 9),
        Asignatura("E901", "Emprendedores", 3, 9),
        Asignatura("CE1001", "Culminación de estudios", 4, 10),
        Asignatura("AIMD1001", "Automatización inteligente y minería de datos", 4, 10),
        Asignatura("PPII1001", "Prácticas profesionales II", 4, 10),

    ]
        

        for m in lista_sistemas:
            materias_sistemas[m.codigo] = m
            grafo_sistemas.agregar_materia(m.codigo)

        grafo_sistemas.agregar_relacion("A1CE101", "A2CE201")
        grafo_sistemas.agregar_relacion("A2CE201", "A2PCE301")
        grafo_sistemas.agregar_relacion("A2PCE301", "B1CE401")
        grafo_sistemas.agregar_relacion("B1CE401", "B1PCE501")
        grafo_sistemas.agregar_relacion("B1PCE501", "B2CE601")

        grafo_sistemas.agregar_relacion("MB101", "C201")
        grafo_sistemas.agregar_relacion("C201", "CII301")
        grafo_sistemas.agregar_relacion("CII301", "AL401")
        grafo_sistemas.agregar_relacion("CII301", "FA501")
        grafo_sistemas.agregar_relacion("MB101", "E301")

        grafo_sistemas.agregar_relacion("IP101", "PE201")
        grafo_sistemas.agregar_relacion("PE201", "POO301")
        grafo_sistemas.agregar_relacion("POO301", "PAD401")
        grafo_sistemas.agregar_relacion("POO301", "DAM501")
        grafo_sistemas.agregar_relacion("DAM501", "DAMII601")
        grafo_sistemas.agregar_relacion("POO301", "DWF501")
        grafo_sistemas.agregar_relacion("DWF501", "DWB601")
        grafo_sistemas.agregar_relacion("POO301", "DAMI501")
        grafo_sistemas.agregar_relacion("DAMI501", "DAMMII601")
        grafo_sistemas.agregar_relacion("ADS201", "IS501")
        grafo_sistemas.agregar_relacion("IS501", "ISII601")
        grafo_sistemas.agregar_relacion("ISII601", "GPT901")

        grafo_sistemas.agregar_relacion("PE201", "BD301")
        grafo_sistemas.agregar_relacion("BD301", "ADB401")
        grafo_sistemas.agregar_relacion("ADB401", "SII801")
        grafo_sistemas.agregar_relacion("POO301", "FIA701")
        grafo_sistemas.agregar_relacion("E301", "FIA701")
        grafo_sistemas.agregar_relacion("FIA701", "ML801")
        grafo_sistemas.agregar_relacion("ML801", "RN901")
        grafo_sistemas.agregar_relacion("RN901", "AIMD1001")

        grafo_sistemas.agregar_relacion("ITIC101", "TDR301")
        grafo_sistemas.agregar_relacion("TDR301", "TDRII401")
        grafo_sistemas.agregar_relacion("TDRII401", "ADS501")
        grafo_sistemas.agregar_relacion("ADS501", "SD701")
        grafo_sistemas.agregar_relacion("TDRII401", "SLI701")
        grafo_sistemas.agregar_relacion("SLI701", "AI801")
        grafo_sistemas.agregar_relacion("PPI901", "PPII1001")
        grafo_sistemas.agregar_relacion("MDI301", "CE1001")

        self.carreras["Ingenieria en Sistemas"] = {
            "materias": materias_sistemas,
            "grafo": grafo_sistemas
        }
        materias_medicina = {}
        grafo_medicina = Grafo()

        lista_medicina = [
        Asignatura("CYL101", "Comunicación y Lenguaje I", 3, 1),
        Asignatura("A1CE101", "A1 Communicative English", 3, 1),
        Asignatura("QO101", "Química Orgánica", 4, 1),
        Asignatura("BMC101", "Biología Molecular y Celular", 4, 1),
        Asignatura("A101", "Anatomía I", 4, 1),
        Asignatura("EA101", "Educación Ambiental", 3, 1),
        Asignatura("INOP101", "Identidad Nacional y Orgullo Patrio", 3, 1),
        Asignatura("CYL201", "Comunicación y Lenguaje II", 3, 2),
        Asignatura("A2CE201", "A2 Communicative English", 3, 2),
        Asignatura("PIU201", "Proyección e Integración Universitaria", 3, 2),
        Asignatura("HIN201", "Historia e Identidad Nacional", 3, 2),
        Asignatura("AII201", "Anatomía II", 4, 2),
        Asignatura("IPM201", "Introducción a las Prácticas Médicas", 4, 2),
        Asignatura("BF201", "Biofísica", 4, 2),
        Asignatura("A2PCE301", "A2+ Communicative English", 3, 3),
        Asignatura("S301", "Sociología", 3, 3),
        Asignatura("E301", "Embriología", 4, 3),
        Asignatura("PM301", "Psicología Médica", 3, 3),
        Asignatura("FI301", "Fisiología I", 4, 3),
        Asignatura("B301", "Bioquímica", 4, 3),
        Asignatura("BE301", "Bioestadística", 4, 3),
        Asignatura("B1CE401", "B1 Communicative English", 3, 4),
        Asignatura("DM401", "Deontología Médica", 3, 4),
        Asignatura("FII401", "Fisiología II", 4, 4),
        Asignatura("H401", "Histología", 4, 4),
        Asignatura("I401", "Inmunología", 4, 4),
        Asignatura("SCI401", "Salud Comunitaria I", 4, 4),
        Asignatura("EPI401", "Epidemiología", 4, 4),
        Asignatura("B1PCE501", "B1+ Communicative English", 3, 5),
        Asignatura("P501", "Patología", 4, 5),
        Asignatura("M501", "Microbiología", 4, 5),
        Asignatura("SI501", "Semiología I", 4, 5),
        Asignatura("FI501", "Farmacología I", 4, 5),
        Asignatura("SCII501", "Salud Comunitaria II", 4, 5),
        Asignatura("BM501", "Biomatemáticas", 3, 5),
        Asignatura("B2CE601", "B2 Communicative English", 3, 6),
        Asignatura("P601", "Parasitología", 4, 6),
        Asignatura("SII601", "Semiología II", 4, 6),
        Asignatura("FII601", "Farmacología II", 4, 6),
        Asignatura("FSP601", "Fisiopatología", 4, 6),
        Asignatura("SCIII601", "Salud Comunitaria III", 4, 6),
        Asignatura("MDI601", "Metodología de la Investigación", 3, 6),
        Asignatura("MI701", "Medicina Interna", 4, 7),
        Asignatura("PHMI701", "Prácticas Hospitalarias de Medicina Interna", 4, 7),
        Asignatura("T701", "Toxicología", 4, 7),
        Asignatura("ORL701", "Otorrinolaringología", 4, 7),
        Asignatura("MLF701", "Medicina Legal y Forense", 4, 7),
        Asignatura("PSI701", "Psiquiatría", 4, 7),
        Asignatura("C801", "Cirugía", 4, 8),
        Asignatura("PHC801", "Prácticas Hospitalarias de Cirugía", 4, 8),
        Asignatura("O801", "Oftalmología", 4, 8),
        Asignatura("NC801", "Nutrición Clínica", 4, 8),
        Asignatura("I801", "Imagenología", 4, 8),
        Asignatura("G801", "Genética", 4, 8),
        Asignatura("GO901", "Ginecología y Obstetricia", 4, 9),
        Asignatura("PHGO901", "Prácticas Hospitalarias de Ginecología y Obstetricia", 4, 9),
        Asignatura("PI901", "Proyecto de Investigación I", 3, 9),
        Asignatura("AS901", "Administración en Salud", 3, 9),
        Asignatura("E901", "Emprendedores", 3, 9),
        Asignatura("P1001", "Pediatría", 4, 10),
        Asignatura("PHP1001", "Prácticas Hospitalarias de Pediatría", 4, 10),
        Asignatura("D1001", "Dermatología", 4, 10),
        Asignatura("MO1001", "Medicina Ocupacional", 3, 10),
        Asignatura("PII1001", "Proyecto de Investigación II", 3, 10),
        Asignatura("IRAMA1101", "Internado Rotatorio en Atención Médica del Adulto", 4, 11),
        Asignatura("IRACA1101", "Internado Rotatorio en Atención Quirúrgica del Adulto", 4, 11),
        Asignatura("IRAM1101", "Internado Rotatorio en Atención a la Mujer", 4, 11),
        Asignatura("IRAIN1201", "Internado Rotatorio en Atención Integral al Niño y la Niña", 4, 12),
        Asignatura("IRASFC1201", "Internado Rotatorio en Atención a la Salud Familiar y Comunitaria", 4, 12),
        Asignatura("FCEMG1201", "Forma de Culminación de Estudios Medicina General", 4, 12),

]
        for m in lista_medicina:
            materias_medicina[m.codigo] = m
            grafo_medicina.agregar_materia(m.codigo)
        
        grafo_medicina.agregar_relacion("A1CE101", "A2CE201")
        grafo_medicina.agregar_relacion("A2CE201", "A2PCE301")
        grafo_medicina.agregar_relacion("A2PCE301", "B1CE401")
        grafo_medicina.agregar_relacion("B1CE401", "B1PCE501")
        grafo_medicina.agregar_relacion("B1PCE501", "B2CE601")

        grafo_medicina.agregar_relacion("A101", "AII201")
        grafo_medicina.agregar_relacion("AII201", "E301")
        grafo_medicina.agregar_relacion("BMC101", "E301")
        grafo_medicina.agregar_relacion("BMC101", "H401")
        grafo_medicina.agregar_relacion("AII201", "H401")
        grafo_medicina.agregar_relacion("H401", "P501")
        grafo_medicina.agregar_relacion("AII201", "I801")
        grafo_medicina.agregar_relacion("BF201", "FI301")
        grafo_medicina.agregar_relacion("FI301", "FII401")
        grafo_medicina.agregar_relacion("FII401", "FSP601")
        grafo_medicina.agregar_relacion("QO101", "B301")
        grafo_medicina.agregar_relacion("B301", "FI501")
        grafo_medicina.agregar_relacion("FI501", "FII601")
        grafo_medicina.agregar_relacion("IPM201", "SI501")
        grafo_medicina.agregar_relacion("SI501", "SII601")

        grafo_medicina.agregar_relacion("SCI401", "SCII501")
        grafo_medicina.agregar_relacion("SCII501", "SCIII601")
        grafo_medicina.agregar_relacion("SII601", "MI701")
        grafo_medicina.agregar_relacion("SII601", "PHMI701")
        grafo_medicina.agregar_relacion("MI701", "C801")
        grafo_medicina.agregar_relacion("PHMI701", "PHC801")
        grafo_medicina.agregar_relacion("C801", "GO901")
        grafo_medicina.agregar_relacion("PHC801", "PHGO901")
        grafo_medicina.agregar_relacion("GO901", "P1001")
        grafo_medicina.agregar_relacion("PHGO901", "PHP1001")
        grafo_medicina.agregar_relacion("MDI601", "PI901")
        grafo_medicina.agregar_relacion("PI901", "PII1001")
        grafo_medicina.agregar_relacion("PII1001", "FCEMG1201")
        grafo_medicina.agregar_relacion("IRAMA1101", "IRAIN1201")


        self.carreras["Medicina General"] = {
            "materias": materias_medicina,
            "grafo": grafo_medicina
                }

        materias_arquitectura = {}
        grafo_arquitectura = Grafo()
        
        lista_arquitectura = [
        Asignatura("CYL101", "Comunicación y Lenguaje I", 3, 1),
        Asignatura("EPSI101", "Electiva Proyección Social I", 3, 1),
        Asignatura("ED101", "Electiva Deporte", 3, 1),
        Asignatura("EC101", "Electiva Cultura", 3, 1),
        Asignatura("EPSII101", "Electiva Proyección Social II", 3, 1),
        Asignatura("A1CE101", "A1 Communicative English", 3, 1),
        Asignatura("DT101", "Dibujo Técnico", 4, 1),
        Asignatura("MB101", "Matemática Básica", 4, 1),
        Asignatura("DAI101", "Diseño Arquitectónico I", 4, 1),
        Asignatura("LE101", "Lógica Estructural", 4, 1),
        Asignatura("G101", "Geología", 3, 1),
        Asignatura("EAF101", "Electiva Actividad de Facultad", 3, 1),
        Asignatura("INOP101", "Identidad Nacional y Orgullo Patrio", 3, 1),
        Asignatura("IHTA201", "Introducción a la Historia y Teoría de la Arquitectura", 4, 2),
        Asignatura("GD201", "Geometría Descriptiva I", 4, 2),
        Asignatura("CYL201", "Comunicación y Lenguaje II", 3, 2),
        Asignatura("A2CE201", "A2 Communicative English", 3, 2),
        Asignatura("C201", "Cálculo I", 4, 2),
        Asignatura("DAII201", "Diseño Arquitectónico II", 4, 2),
        Asignatura("TDAI201", "Taller Digital Arquitectónico I", 4, 2),
        Asignatura("HIN201", "Historia e Identidad Nacional", 3, 2),
        Asignatura("A2PCE301", "A2+ Communicative English", 3, 3),
        Asignatura("TDAII301", "Taller Digital Arquitectónico II", 4, 3),
        Asignatura("DAIII301", "Diseño Arquitectónico III", 4, 3),
        Asignatura("T301", "Topografía", 4, 3),
        Asignatura("E301", "Estadística I", 4, 3),
        Asignatura("FIS301", "Física I", 4, 3),
        Asignatura("HTAI301", "Historia y Teoría de la Arquitectura I", 4, 3),
        Asignatura("HTAII401", "Historia y Teoría de la Arquitectura II", 4, 4),
        Asignatura("MDI401", "Metodología de la Investigación", 3, 4),
        Asignatura("B1CE401", "B1 Communicative English", 3, 4),
        Asignatura("DAIV401", "Diseño Arquitectónico IV", 4, 4),
        Asignatura("EI401", "Electiva I", 3, 4),
        Asignatura("MC401", "Materiales de Construcción", 4, 4),
        Asignatura("GDII401", "Geometría Descriptiva II", 4, 4),
        Asignatura("E501", "Estructura I", 4, 5),
        Asignatura("B1PCE501", "B1+ Communicative English", 3, 5),
        Asignatura("HTAIII501", "Historia y Teoría de la Arquitectura III", 4, 5),
        Asignatura("SCI501", "Sistemas Constructivos I", 4, 5),
        Asignatura("DAV501", "Diseño Arquitectónico V", 4, 5),
        Asignatura("IE501", "Instalaciones en Edificaciones", 4, 5),
        Asignatura("UAI501", "Urbanismo y Ambiente I", 4, 5),
        Asignatura("B2CE601", "B2 Communicative English", 3, 6),
        Asignatura("EII601", "Estructura II", 4, 6),
        Asignatura("SCII601", "Sistemas Constructivos II", 4, 6),
        Asignatura("TCA601", "Teoría y Crítica de la Arquitectura", 4, 6),
        Asignatura("UAII601", "Urbanismo y Ambiente II", 4, 6),
        Asignatura("G601", "Geodesia", 4, 6),
        Asignatura("DAVII601", "Diseño Arquitectónico VI", 4, 6),
        Asignatura("EIII701", "Estructura III", 4, 7),
        Asignatura("EM701", "Emprendedores", 3, 7),
        Asignatura("AB701", "Arquitectura Bioclimática", 4, 7),
        Asignatura("UAIII701", "Urbanismo y Ambiente III", 4, 7),
        Asignatura("LP701", "Lógica Paramétrica", 4, 7),
        Asignatura("CPLO701", "Costo, Presupuesto y Licitación de Obras", 4, 7),
        Asignatura("DAVII701", "Diseño Arquitectónico VII", 4, 7),
        Asignatura("UAIV801", "Urbanismo y Ambiente IV", 4, 8),
        Asignatura("DAVIII801", "Diseño Arquitectónico VIII", 4, 8),
        Asignatura("FVA801", "Factibilidad y Valoración Ambiental", 4, 8),
        Asignatura("GP801", "Gerencia de Proyecto", 4, 8),
        Asignatura("EII801", "Electiva II", 3, 8),
        Asignatura("PPI801", "Prácticas Profesionales I", 4, 8),
        Asignatura("EIII901", "Electiva III", 3, 9),
        Asignatura("PPII901", "Prácticas Profesionales II", 4, 9),
        Asignatura("DAIX901", "Diseño Arquitectónico IX", 4, 9),
        Asignatura("RS901", "Responsabilidad Social", 3, 9),
        Asignatura("IS901", "Ingeniería Sismorresistente", 4, 9),
        Asignatura("PCP901", "Principios de Conservación del Patrimonio", 4, 9),
        Asignatura("ECE1001", "Electiva Culminación de Estudios", 4, 10),
        ]

        
        for m in lista_arquitectura:
            materias_arquitectura[m.codigo] = m
            grafo_arquitectura.agregar_materia(m.codigo)

        grafo_arquitectura.agregar_relacion("A1CE101", "A2CE201")
        grafo_arquitectura.agregar_relacion("A2CE201", "A2PCE301")
        grafo_arquitectura.agregar_relacion("A2PCE301", "B1CE401")
        grafo_arquitectura.agregar_relacion("B1CE401", "B1PCE501")
        grafo_arquitectura.agregar_relacion("B1PCE501", "B2CE601")
        grafo_arquitectura.agregar_relacion("CYL101", "CYL201")

        grafo_arquitectura.agregar_relacion("DAI101", "DAII201")
        grafo_arquitectura.agregar_relacion("DAII201", "DAIII301")
        grafo_arquitectura.agregar_relacion("DAIII301", "DAIV401")
        grafo_arquitectura.agregar_relacion("DAIV401", "DAV501")
        grafo_arquitectura.agregar_relacion("DAV501", "DAVII601")
        grafo_arquitectura.agregar_relacion("DAVII601", "DAVII701")
        grafo_arquitectura.agregar_relacion("DAVII701", "DAVIII801")
        grafo_arquitectura.agregar_relacion("DAVIII801", "DAIX901")
        grafo_arquitectura.agregar_relacion("DAIX901", "ECE1001")

        grafo_arquitectura.agregar_relacion("DT101", "GD201")
        grafo_arquitectura.agregar_relacion("GD201", "GDII401")
        grafo_arquitectura.agregar_relacion("DT101", "TDAI201")
        grafo_arquitectura.agregar_relacion("TDAI201", "TDAII301")
        grafo_arquitectura.agregar_relacion("TDAII301", "LP701")
        grafo_arquitectura.agregar_relacion("MB101", "C201")
        grafo_arquitectura.agregar_relacion("C201", "FIS301")
        grafo_arquitectura.agregar_relacion("LE101", "E501")
        grafo_arquitectura.agregar_relacion("FIS301", "E501")
        grafo_arquitectura.agregar_relacion("E501", "EII601")
        grafo_arquitectura.agregar_relacion("EII601", "EIII701")
        grafo_arquitectura.agregar_relacion("EIII701", "IS901")

        grafo_arquitectura.agregar_relacion("IHTA201", "HTAI301")
        grafo_arquitectura.agregar_relacion("HTAI301", "HTAII401")
        grafo_arquitectura.agregar_relacion("HTAII401", "HTAIII501")
        grafo_arquitectura.agregar_relacion("HTAIII501", "TCA601")
        grafo_arquitectura.agregar_relacion("MC401", "SCI501")
        grafo_arquitectura.agregar_relacion("SCI501", "SCII601")
        grafo_arquitectura.agregar_relacion("UAI501", "UAII601")
        grafo_arquitectura.agregar_relacion("UAII601", "UAIII701")
        grafo_arquitectura.agregar_relacion("UAIII701", "UAIV801")
        grafo_arquitectura.agregar_relacion("T301", "G601")
        grafo_arquitectura.agregar_relacion("PPI801", "PPII901")

        self.carreras["Arquitectura"] = {
            "materias": materias_arquitectura,
            "grafo": grafo_arquitectura
                }

        materias_civil = {}
        grafo_civil = Grafo()
                
        lista_civil = [
        Asignatura("MB101", "Matemática Básica", 4, 1),
        Asignatura("DTC101", "Dibujo Técnico para Ingeniería Civil", 4, 1),
        Asignatura("A1CE101", "A1 Communicative English", 3, 1),
        Asignatura("CYL101", "Comunicación y Lenguaje I", 3, 1),
        Asignatura("PIU101", "Proyección e Integración Universitaria", 3, 1),
        Asignatura("M101", "Multiculturalidad", 3, 1),
        Asignatura("INOP101", "Identidad Nacional y Orgullo Patrio", 3, 1),
        Asignatura("EA101", "Educación Ambiental", 3, 1),
        Asignatura("C201", "Cálculo I", 4, 2),
        Asignatura("PIC201", "Principios de Ingeniería Civil", 4, 2),
        Asignatura("FIS201", "Física I", 4, 2),
        Asignatura("GD201", "Geometría Descriptiva I", 4, 2),
        Asignatura("A2CE201", "A2 Communicative English", 3, 2),
        Asignatura("CYL201", "Comunicación y Lenguaje II", 3, 2),
        Asignatura("HIN201", "Historia e Identidad Nacional", 3, 2),
        Asignatura("LE301", "Lógica Estructural", 4, 3),
        Asignatura("CII301", "Cálculo II", 4, 3),
        Asignatura("FISII301", "Física II", 4, 3),
        Asignatura("DAC301", "Dibujo Asistido por Computadoras", 4, 3),
        Asignatura("A2PCE301", "A2+ Communicative English", 3, 3),
        Asignatura("TB301", "Topografía Básica", 4, 3),
        Asignatura("E401", "Estadística I", 4, 4),
        Asignatura("MS401", "Mecánica de Suelos", 4, 4),
        Asignatura("AV401", "Análisis Vectorial", 4, 4),
        Asignatura("G401", "Geodesia", 4, 4),
        Asignatura("B1CE401", "B1 Communicative English", 3, 4),
        Asignatura("EA401", "Estática Aplicada", 4, 4),
        Asignatura("TA401", "Topografía Aplicada", 4, 4),
        Asignatura("G501", "Geotecnia", 4, 5),
        Asignatura("EDO501", "Ecuaciones Diferenciales Ordinarias", 4, 5),
        Asignatura("B1PCE501", "B1+ Communicative English", 3, 5),
        Asignatura("MC501", "Materiales de Construcción", 4, 5),
        Asignatura("MMA501", "Mecánica de Materiales", 4, 5),
        Asignatura("SEC501", "Sistemas y Equipos de Construcción", 4, 5),
        Asignatura("IT501", "Ingeniería de Tránsito", 4, 5),
        Asignatura("DA601", "Dinámica Aplicada", 4, 6),
        Asignatura("MDI601", "Metodología de la Investigación", 3, 6),
        Asignatura("IE601", "Instalaciones en Edificaciones", 4, 6),
        Asignatura("B2CE601", "B2 Communicative English", 3, 6),
        Asignatura("AEI601", "Análisis Estructural I", 4, 6),
        Asignatura("PT601", "Planificación del Transporte", 4, 6),
        Asignatura("H601", "Hidrología", 4, 6),
        Asignatura("IE701", "Ingeniería Económica", 4, 7),
        Asignatura("AEII701", "Análisis Estructural II", 4, 7),
        Asignatura("DEMA701", "Diseño Estructural de Madera y Acero", 4, 7),
        Asignatura("DGV701", "Diseño Geométrico de Vías", 4, 7),
        Asignatura("IA701", "Innovación Abierta", 3, 7),
        Asignatura("MF701", "Mecánica de Fluidos I", 4, 7),
        Asignatura("CP801", "Costos y Presupuesto", 4, 8),
        Asignatura("DCI801", "Diseño de Concreto I", 4, 8),
        Asignatura("DM801", "Diseño de Mampostería", 4, 8),
        Asignatura("DP801", "Diseño de Pavimentos", 4, 8),
        Asignatura("HA801", "Hidráulica Aplicada", 4, 8),
        Asignatura("PPI801", "Prácticas Profesionales I", 4, 8),
        Asignatura("DCII901", "Diseño de Concreto II", 4, 9),
        Asignatura("PCP901", "Planificación y Control de Proyectos", 4, 9),
        Asignatura("IS901", "Ingeniería Sanitaria", 4, 9),
        Asignatura("E901", "Emprendedores", 3, 9),
        Asignatura("PPII901", "Prácticas Profesionales II", 4, 9),
        Asignatura("SGA1001", "Sistemas de Gestión Ambiental", 4, 10),
        Asignatura("IS1001", "Ingeniería Sismorresistente", 4, 10),
        Asignatura("FCE1001", "Formas de Culminación de Estudios", 4, 10),

    ]
        for m in lista_civil:
            materias_civil[m.codigo] = m
            grafo_civil.agregar_materia(m.codigo)

        grafo_civil.agregar_relacion("A1CE101", "A2CE201")
        grafo_civil.agregar_relacion("A2CE201", "A2PCE301")
        grafo_civil.agregar_relacion("A2PCE301", "B1CE401")
        grafo_civil.agregar_relacion("B1CE401", "B1PCE501")
        grafo_civil.agregar_relacion("B1PCE501", "B2CE601")
        grafo_civil.agregar_relacion("CYL101", "CYL201")

        grafo_civil.agregar_relacion("MB101", "C201")
        grafo_civil.agregar_relacion("C201", "CII301")
        grafo_civil.agregar_relacion("CII301", "AV401")
        grafo_civil.agregar_relacion("CII301", "EDO501")
        grafo_civil.agregar_relacion("C201", "FIS201")
        grafo_civil.agregar_relacion("FIS201", "FISII301")

        grafo_civil.agregar_relacion("FIS201", "LE301")
        grafo_civil.agregar_relacion("LE301", "EA401")
        grafo_civil.agregar_relacion("EA401", "MMA501")
        grafo_civil.agregar_relacion("MMA501", "AEI601")
        grafo_civil.agregar_relacion("AEI601", "AEII701")
        grafo_civil.agregar_relacion("AEII701", "DEMA701")
        grafo_civil.agregar_relacion("AEII701", "DCI801")
        grafo_civil.agregar_relacion("DCI801", "DCII901")
        grafo_civil.agregar_relacion("DCII901", "IS1001")
        grafo_civil.agregar_relacion("DTC101", "DAC301")

        grafo_civil.agregar_relacion("TB301", "TA401")
        grafo_civil.agregar_relacion("TB301", "G401")
        grafo_civil.agregar_relacion("TA401", "DGV701")
        grafo_civil.agregar_relacion("MS401", "G501")
        grafo_civil.agregar_relacion("FISII301", "DA601")
        grafo_civil.agregar_relacion("FISII301", "MF701")
        grafo_civil.agregar_relacion("MF701", "HA801")
        grafo_civil.agregar_relacion("HA801", "IS901")
        grafo_civil.agregar_relacion("PPI801", "PPII901")
        grafo_civil.agregar_relacion("MDI601", "FCE1001")
                        
        self.carreras["Ingenieria Civil"] = {
            "materias": materias_civil,
            "grafo": grafo_civil
                }

        materias_industrial = {}
        grafo_industrial = Grafo()
                        
        lista_industrial = [
        Asignatura("MB101", "Matemática Básica", 4, 1),
        Asignatura("CYL101", "Comunicación y Lenguaje I", 3, 1),
        Asignatura("A1CE101", "A1 Communicative English", 3, 1),
        Asignatura("III101", "Introducción a la Ingeniería Industrial", 4, 1),
        Asignatura("Q101", "Química", 4, 1),
        Asignatura("ED101", "Electiva Deporte", 3, 1),
        Asignatura("EC101", "Electiva Cultura", 3, 1),
        Asignatura("EPSI101", "Electiva Proyección Social I", 3, 1),
        Asignatura("INOP101", "Identidad Nacional y Orgullo Patrio", 3, 1),
        Asignatura("EI101", "Electiva I", 3, 1),
        Asignatura("EPSII201", "Electiva Proyección Social II", 3, 2),
        Asignatura("C201", "Cálculo I", 4, 2),
        Asignatura("CYL201", "Comunicación y Lenguaje II", 3, 2),
        Asignatura("A2CE201", "A2 Communicative English", 3, 2),
        Asignatura("C201B", "Contabilidad I", 4, 2),
        Asignatura("EII201", "Electiva II", 3, 2),
        Asignatura("HIN201", "Historia e Identidad Nacional", 3, 2),
        Asignatura("EDS201", "Ecología y Desarrollo Sostenible", 3, 2),
        Asignatura("E301", "Estadística I", 4, 3),
        Asignatura("A2PCE301", "A2+ Communicative English", 3, 3),
        Asignatura("ET301", "Estudio del Trabajo", 4, 3),
        Asignatura("CII301", "Cálculo II", 4, 3),
        Asignatura("CC301", "Contabilidad de Costos", 4, 3),
        Asignatura("EIII301", "Electiva III", 3, 3),
        Asignatura("EDO401", "Ecuaciones Diferenciales Ordinarias", 4, 4),
        Asignatura("F401", "Finanzas", 4, 4),
        Asignatura("EII401", "Estadística II", 4, 4),
        Asignatura("GRH401", "Gestión de Recursos Humanos", 4, 4),
        Asignatura("B1CE401", "B1 Communicative English", 3, 4),
        Asignatura("EAF401", "Electiva Actividades de Facultad", 3, 4),
        Asignatura("FIS401", "Física I", 4, 4),
        Asignatura("MDI501", "Metodología de la Investigación", 3, 5),
        Asignatura("CEC501", "Control Estadístico de la Calidad", 4, 5),
        Asignatura("IE501", "Ingeniería Económica", 4, 5),
        Asignatura("EIV501", "Electiva IV", 3, 5),
        Asignatura("B1PCE501", "B1+ Communicative English", 3, 5),
        Asignatura("RS501", "Responsabilidad Social", 3, 5),
        Asignatura("B2CE601", "B2 Communicative English", 3, 6),
        Asignatura("GC601", "Gestión de la Calidad", 4, 6),
        Asignatura("FISII601", "Física II", 4, 6),
        Asignatura("DSP601", "Diseño de Sistemas de Producción", 4, 6),
        Asignatura("IDO601", "Investigación de Operaciones I", 4, 6),
        Asignatura("EE601", "Estrategia Empresarial", 4, 6),
        Asignatura("IDOII701", "Investigación de Operaciones II", 4, 7),
        Asignatura("E701", "Emprendedores", 3, 7),
        Asignatura("PM701", "Procesos de Manufactura", 4, 7),
        Asignatura("IE701", "Instalaciones Eléctricas", 4, 7),
        Asignatura("MF701", "Mecánica de Fluidos I", 4, 7),
        Asignatura("MI801", "Máquinas Industriales", 4, 8),
        Asignatura("PCP801", "Planeamiento y Control de la Producción", 4, 8),
        Asignatura("SHO801", "Seguridad e Higiene Ocupacional", 4, 8),
        Asignatura("T801", "Termodinámica", 4, 8),
        Asignatura("PPI801", "Prácticas Profesionales I", 4, 8),
        Asignatura("DPP801", "Diseño y Presupuesto de Proyectos", 4, 8),
        Asignatura("LMM901", "Logística y Manejo de Materiales", 4, 9),
        Asignatura("PL901", "Producción más Limpia", 4, 9),
        Asignatura("ER901", "Energías Renovables", 4, 9),
        Asignatura("PPII901", "Prácticas Profesionales II", 4, 9),
        Asignatura("SP901", "Simulación de Procesos", 4, 9),
        Asignatura("GP901", "Gerencia de Proyecto", 4, 9),
        Asignatura("ECE1001", "Electiva Culminación de Estudios", 4, 10),

    ]
        for m in lista_industrial:
            materias_industrial[m.codigo] = m
            grafo_industrial.agregar_materia(m.codigo)

        grafo_industrial.agregar_relacion("A1CE101", "A2CE201")
        grafo_industrial.agregar_relacion("A2CE201", "A2PCE301")
        grafo_industrial.agregar_relacion("A2PCE301", "B1CE401")
        grafo_industrial.agregar_relacion("B1CE401", "B1PCE501")
        grafo_industrial.agregar_relacion("B1PCE501", "B2CE601")
        grafo_industrial.agregar_relacion("CYL101", "CYL201")

        grafo_industrial.agregar_relacion("MB101", "C201")
        grafo_industrial.agregar_relacion("C201", "CII301")
        grafo_industrial.agregar_relacion("CII301", "EDO401")
        grafo_industrial.agregar_relacion("C201", "FIS401")
        grafo_industrial.agregar_relacion("FIS401", "FISII601")
        grafo_industrial.agregar_relacion("FISII601", "MF701")
        grafo_industrial.agregar_relacion("FISII601", "T801")
        grafo_industrial.agregar_relacion("C201", "E301")
        grafo_industrial.agregar_relacion("E301", "EII401")
        grafo_industrial.agregar_relacion("EII401", "CEC501")
        grafo_industrial.agregar_relacion("CEC501", "GC601")

        grafo_industrial.agregar_relacion("C201B", "CC301")
        grafo_industrial.agregar_relacion("CC301", "F401")
        grafo_industrial.agregar_relacion("F401", "IE501")
        grafo_industrial.agregar_relacion("EII401", "IDO601")
        grafo_industrial.agregar_relacion("IDO601", "IDOII701")
        grafo_industrial.agregar_relacion("IDOII701", "SP901")
        grafo_industrial.agregar_relacion("III101", "ET301")
        grafo_industrial.agregar_relacion("ET301", "DSP601")
        grafo_industrial.agregar_relacion("DSP601", "PCP801")
        grafo_industrial.agregar_relacion("PCP801", "LMM901")
        grafo_industrial.agregar_relacion("PPI801", "PPII901")
        grafo_industrial.agregar_relacion("MDI501", "ECE1001")
                        
        self.carreras["Ingenieria Industrial"] = {
            "materias": materias_industrial,
            "grafo": grafo_industrial
                }

        materias_derecho = {}
        grafo_derecho = Grafo()
                        
        lista_derecho = [
        Asignatura("CYL101", "Comunicación y Lenguaje I", 3, 1),
        Asignatura("ACE101", "A1 Communicative English", 3, 1),
        Asignatura("DR101", "Derecho Romano", 4, 1),
        Asignatura("HED101", "Historia del Estado y el Derecho", 4, 1),
        Asignatura("IED101", "Introducción al Estudio del Derecho I", 4, 1),
        Asignatura("INOP101", "Identidad Nacional y Orgullo Patrio", 3, 1),
        Asignatura("PIU101", "Proyección e Integración Universitaria", 3, 1),
        Asignatura("CYL201", "Comunicación y Lenguaje II", 3, 2),
        Asignatura("A2CE201", "A2 Communicative English", 3, 2),
        Asignatura("TGE201", "Teoría General del Estado", 4, 2),
        Asignatura("GP201", "Género y Poder", 3, 2),
        Asignatura("DCI201", "Derecho Constitucional I (Parte General)", 4, 2),
        Asignatura("IEDII201", "Introducción al Estudio del Derecho II", 4, 2),
        Asignatura("HIN201", "Historia e Identidad Nacional", 3, 2),
        Asignatura("DCII301", "Derecho Constitucional II (Parte Especial)", 4, 3),
        Asignatura("A2PCE301", "A2+ Communicative English", 3, 3),
        Asignatura("DPI301", "Derecho Penal I (Parte General)", 4, 3),
        Asignatura("DF301", "Derecho de Familia", 4, 3),
        Asignatura("DAI301", "Derecho Administrativo I (Parte General)", 4, 3),
        Asignatura("DAII401", "Derecho Administrativo II (Parte Especial)", 4, 4),
        Asignatura("B1CE401", "B1 Communicative English", 3, 4),
        Asignatura("TGDP401", "Teoría General del Derecho Procesal", 4, 4),
        Asignatura("DB401", "Derecho de Bienes", 4, 4),
        Asignatura("DPII401", "Derecho Penal II (Parte Especial)", 4, 4),
        Asignatura("DO401", "Derecho de Obligaciones", 4, 4),
        Asignatura("MDI401", "Metodología de la Investigación", 3, 4),
        Asignatura("DPCI501", "Derecho Procesal Civil I", 4, 5),
        Asignatura("B1PCE501", "B1+ Communicative English", 3, 5),
        Asignatura("DMI501", "Derecho Mercantil I", 4, 5),
        Asignatura("DIP501", "Derecho Internacional Público", 4, 5),
        Asignatura("DC501", "Derecho de Contratos", 4, 5),
        Asignatura("DS501", "Derecho de Sucesiones", 4, 5),
        Asignatura("DMII601", "Derecho Mercantil II", 4, 6),
        Asignatura("B2CE601", "B2 Communicative English", 3, 6),
        Asignatura("MARC601", "Métodos Alternos de Resolución de Conflictos", 4, 6),
        Asignatura("DPCII601", "Derecho Procesal Civil II", 4, 6),
        Asignatura("DPP601", "Derecho Procesal Penal I", 4, 6),
        Asignatura("DL601", "Derecho Laboral", 4, 6),
        Asignatura("E701", "Emprendedores", 3, 7),
        Asignatura("DSS701", "Derecho de la Seguridad Social", 4, 7),
        Asignatura("DCOM701", "Derecho Comunitario", 4, 7),
        Asignatura("PPC701", "Práctica Procesal Civil", 4, 7),
        Asignatura("SPDH701", "Sistema de Protección de los Derechos Humanos", 4, 7),
        Asignatura("DPPII701", "Derecho Procesal Penal II", 4, 7),
        Asignatura("ML801", "Medicina Legal", 4, 8),
        Asignatura("DNI801", "Derecho Notarial I", 4, 8),
        Asignatura("DIPR801", "Derecho Internacional Privado", 4, 8),
        Asignatura("DPF801", "Derecho Procesal de Familia", 4, 8),
        Asignatura("TOL801", "Técnicas de Oralidad y Litigación", 4, 8),
        Asignatura("DPPLSS801", "Derecho Procesal Laboral y de la Seguridad Social", 4, 8),
        Asignatura("DCOMP801", "Derecho de la Competencia", 4, 8),
        Asignatura("DJ901", "Deontología Jurídica", 3, 9),
        Asignatura("DNII901", "Derecho Notarial II", 4, 9),
        Asignatura("DPIE901", "Derecho de la Propiedad Intelectual", 4, 9),
        Asignatura("DT901", "Derecho Tributario", 4, 9),
        Asignatura("DR901", "Derecho Registral", 4, 9),
        Asignatura("DB901", "Derecho Bancario", 4, 9),
        Asignatura("PP901", "Práctica Profesional", 4, 9),
        Asignatura("FD1001", "Filosofía del Derecho", 3, 10),
        Asignatura("PN1001", "Práctica Notarial", 4, 10),
        Asignatura("DNI1001", "Derecho de los Negocios Internacionales", 4, 10),
        Asignatura("DA1001", "Derecho Ambiental", 4, 10),
        Asignatura("DAdu1001", "Derecho Aduanero", 4, 10),
        Asignatura("PTRYRI1001", "Práctica Tributaria y Régimen de Inversiones", 4, 10),
        Asignatura("FCE1001", "Formas de Culminación de Estudio", 4, 10),
        ]
        for m in lista_derecho:
            materias_derecho[m.codigo] = m
            grafo_derecho.agregar_materia(m.codigo)

        grafo_derecho.agregar_relacion("ACE101", "A2CE201")
        grafo_derecho.agregar_relacion("A2CE201", "A2PCE301")
        grafo_derecho.agregar_relacion("A2PCE301", "B1CE401")
        grafo_derecho.agregar_relacion("B1CE401", "B1PCE501")
        grafo_derecho.agregar_relacion("B1PCE501", "B2CE601")
        grafo_derecho.agregar_relacion("CYL101", "CYL201")

        grafo_derecho.agregar_relacion("IED101", "IEDII201")
        grafo_derecho.agregar_relacion("HED101", "TGE201")
        grafo_derecho.agregar_relacion("TGE201", "DCI201")
        grafo_derecho.agregar_relacion("DCI201", "DCII301")
        grafo_derecho.agregar_relacion("DCII301", "DAI301")
        grafo_derecho.agregar_relacion("DAI301", "DAII401")

        grafo_derecho.agregar_relacion("DR101", "DB401")
        grafo_derecho.agregar_relacion("DB401", "DO401")
        grafo_derecho.agregar_relacion("DO401", "DC501")
        grafo_derecho.agregar_relacion("DC501", "DS501")
        grafo_derecho.agregar_relacion("TGDP401", "DPCI501")
        grafo_derecho.agregar_relacion("DPCI501", "DPCII601")
        grafo_derecho.agregar_relacion("DPCII601", "PPC701")
        grafo_derecho.agregar_relacion("DMI501", "DMII601")
        grafo_derecho.agregar_relacion("DNI801", "DNII901")
        grafo_derecho.agregar_relacion("DNII901", "PN1001")
        grafo_derecho.agregar_relacion("DPI301", "DPII401")
        grafo_derecho.agregar_relacion("DPII401", "DPP601")
        grafo_derecho.agregar_relacion("DPP601", "DPPII701")
        grafo_derecho.agregar_relacion("MDI401", "FCE1001")

        self.carreras["Derecho"] = {
            "materias": materias_derecho,
            "grafo": grafo_derecho
                }

        materias_psicologia = {}
        grafo_psicologia = Grafo()

        lista_psicologia = [
        Asignatura("HP", "Historia de la psicología", 3, 1),
        Asignatura("PG", "Psicología general", 4, 1),
        Asignatura("CYL1", "Comunicación y lenguaje I", 3, 1),
        Asignatura("PIU", "Proyección e integración universitaria", 3, 1),
        Asignatura("A1CE", "A1 Communicative english", 3, 1),
        Asignatura("INYOP", "Identidad Nacional y Orgullo Patrio", 3, 1),
        Asignatura("AYFDSN", "Anatomía y fisiología del sistema nervioso", 4, 2),
        Asignatura("MYTP", "Modelos y teorías psicológicas", 4, 2),
        Asignatura("PDD1", "Psicología del desarrollo I", 4, 2),
        Asignatura("CYL2", "Comunicación y lenguaje II", 3, 2),
        Asignatura("PDFTDV", "Práctica de familiarización: Taller de vida", 3, 2),
        Asignatura("A2CE", "A2 Communicative english", 3, 2),
        Asignatura("GTH1", "Gestión de talento humano I", 3, 3),
        Asignatura("PDP", "Psicología de la personalidad", 4, 3),
        Asignatura("PDA", "Psicología del aprendizaje", 4, 3),
        Asignatura("NDLTM", "Neurobiología de los trastornos mentales", 4, 3),
        Asignatura("PDD2", "Psicología del desarrollo II", 4, 3),
        Asignatura("A2+CE", "A2+ Communicative english", 3, 3),
        Asignatura("P1", "Psicopatología I", 4, 4),
        Asignatura("GTH2", "Gestión de talento humano II", 3, 4),
        Asignatura("EEIP", "Evaluación e intervención psicopedagógica", 4, 4),
        Asignatura("OVYP", "Orientación vocacional y profesional", 3, 4),
        Asignatura("PS", "Psicología social", 4, 4),
        Asignatura("B1CE", "B1 Communicative english", 3, 4),
        Asignatura("EPCI", "Evaluación psicológica clínica I", 4, 5),
        Asignatura("PPEIE", "Prácticas profesionalizantes en intervención educativa", 4, 5),
        Asignatura("P2", "Psicopatología II", 4, 5),
        Asignatura("PC", "Psicología comunitaria", 4, 5),
        Asignatura("EPL", "Evaluación psicológica laboral", 3, 5),
        Asignatura("B1+CE", "B1+ Communicative english", 3, 5),
        Asignatura("EPCII", "Evaluación psicológica clínica II", 4, 6),
        Asignatura("PCYP1", "Psicología clínica y psicoterapia I", 4, 6),
        Asignatura("PDLS", "Psicología de la sexualidad", 3, 6),
        Asignatura("DDGPIC", "Dinámicas de grupo para intervención comunitaria", 3, 6),
        Asignatura("PPEIL", "Prácticas profesionalizantes en intervención laboral", 4, 6),
        Asignatura("B2CE", "B2 Communicative english", 3, 6),
        Asignatura("P", "Psicofarmacología", 4, 7),
        Asignatura("PCYP2", "Psicología clínica y psicoterapia II", 4, 7),
        Asignatura("PPEIS", "Prácticas profesionalizantes en intervención social", 4, 7),
        Asignatura("E", "Emprendedores", 3, 7),
        Asignatura("MDI", "Metodología de investigación", 4, 7),
        Asignatura("PPEIC", "Prácticas profesionalizantes en intervención clínica", 4, 8),
        Asignatura("SDS", "Seminario de sistematización", 3, 8),
        Asignatura("B", "Bioética", 3, 8),
        Asignatura("PF", "Psicología forense", 4, 8),
        Asignatura("ECDE", "Electiva culminación de estudios", 4, 9),
        ]

        for m in lista_psicologia:
            materias_psicologia[m.codigo] = m
            grafo_psicologia.agregar_materia(m.codigo)
        
        grafo_psicologia.agregar_relacion("A1CE", "A2CE")
        grafo_psicologia.agregar_relacion("A2CE", "A2+CE")
        grafo_psicologia.agregar_relacion("A2+CE", "B1CE")
        grafo_psicologia.agregar_relacion("B1CE", "B1+CE")
        grafo_psicologia.agregar_relacion("B1+CE", "B2CE")
        grafo_psicologia.agregar_relacion("CYL1", "CYL2")

        grafo_psicologia.agregar_relacion("HP", "MYTP")
        grafo_psicologia.agregar_relacion("PG", "MYTP")
        grafo_psicologia.agregar_relacion("PG", "PDP")
        grafo_psicologia.agregar_relacion("PG", "PDA")
        grafo_psicologia.agregar_relacion("PDD1", "PDD2")
        grafo_psicologia.agregar_relacion("AYFDSN", "NDLTM")
        grafo_psicologia.agregar_relacion("NDLTM", "P1")
        grafo_psicologia.agregar_relacion("P1", "P2")
        grafo_psicologia.agregar_relacion("P2", "P")
        grafo_psicologia.agregar_relacion("GTH1", "GTH2")
        grafo_psicologia.agregar_relacion("P1", "EPCI")
        grafo_psicologia.agregar_relacion("EPCI", "EPCII")
        grafo_psicologia.agregar_relacion("EPCII", "PCYP1")
        grafo_psicologia.agregar_relacion("PCYP1", "PCYP2")
        grafo_psicologia.agregar_relacion("PPEIE", "PPEIL")
        grafo_psicologia.agregar_relacion("PPEIL", "PPEIS")
        grafo_psicologia.agregar_relacion("PPEIS", "PPEIC")
        grafo_psicologia.agregar_relacion("MDI", "ECDE")
               
        self.carreras["Psicologia"] = {
            "materias": materias_psicologia,
            "grafo": grafo_psicologia
                        }

        materias_nutricion = {}
        grafo_nutricion = Grafo()

        lista_nutricion = [
        Asignatura("CYL1", "Comunicación y Lenguaje I", 3, 1,),
        Asignatura("PIU", "Proyección e Integración Universitaria", 3, 1),
        Asignatura("MB", "Matemática Básica", 4, 1),
        Asignatura("IALSC", "Introducción a la Semiótica Clínica", 3, 1),
        Asignatura("A1CE", "A1 Communicative English", 3, 1),
        Asignatura("HEIN", "Historia e identidad nacional", 3, 1),
        Asignatura("INYOP", "Identidad Nacional y Orgullo Patrio", 3, 1),
        Asignatura("CYL2", "Comunicación y Lenguaje II", 3, 2),
        Asignatura("B", "Bioestadística", 4, 2),
        Asignatura("IALB", "Introducción a la Bromatología", 4, 2),
        Asignatura("A", "Anatomofisiología", 4, 2),
        Asignatura("HEIN2", "Historia e Identidad Nacional", 3, 2),
        Asignatura("A2CE", "A2 Communicative English", 3, 2),
        Asignatura("IALGYN", "Introducción a la Genética y Nutrigenómica", 4, 3),
        Asignatura("NH1", "Nutrición Humana I", 4, 3),
        Asignatura("ABN", "Análisis Bioquímico Nutricional", 4, 3),
        Asignatura("EDEL1", "Evaluación del Estado Nutricional I", 4, 3),
        Asignatura("A2+CE", "A2+ Communicative English", 3, 3),
        Asignatura("BI", "Bioética", 3, 4),
        Asignatura("NH2", "Nutrición Humana II", 4, 4),
        Asignatura("FAALN", "Farmacología Aplicada a la Nutrición", 4, 4),
        Asignatura("EDEL2", "Evaluación del Estado Nutricional II", 4, 4),
        Asignatura("E", "Emprendedores", 3, 4),
        Asignatura("B1CE", "B1 Communicative English", 3, 4),
        Asignatura("PDLCA", "Psicología de la Conducta Alimentaria", 3, 5),
        Asignatura("PDF", "Prácticas de Familiarización", 3, 5),
        Asignatura("IALD", "Introducción a la Dietoterapia", 4, 5),
        Asignatura("FN1", "Fisiopatología Nutricional I", 4, 5),
        Asignatura("MEHDLA", "Microbiología e Higiene de los Alimentos", 4, 5),
        Asignatura("B1+CE", "B1+ Communicative English", 3, 5),
        Asignatura("EAN", "Educación Alimentaria Nutricional", 3, 6),
        Asignatura("NMI", "Nutrición Materno Infantil", 4, 6),
        Asignatura("DAINYA", "Dietoterapia a Infantes, Niños y Adolescentes", 4, 6),
        Asignatura("FN2", "Fisiopatología Nutricional II", 4, 6),
        Asignatura("TDLA", "Toxicología de los Alimentos", 4, 6),
        Asignatura("B2CE", "B2 Communicative English", 3, 6),
        Asignatura("MDLI", "Metodología de la Investigación", 4, 7),
        Asignatura("DYPDLAYN", "Diseño y Planeación de la Alimentación y la Nutrición", 4, 7),
        Asignatura("DAYAM", "Dietoterapia de Adultos y Adultos Mayores", 4, 7),
        Asignatura("EAALN", "Epidemiología Aplicada a la Nutrición", 4, 7),
        Asignatura("MAYN", "Marketing Alimentario y Nutricional", 3, 7),
        Asignatura("SYPDA", "Selección y Preparación de Alimentos", 3, 7),
        Asignatura("NDFDAYDE", "Normativas de Fortificación de Alimentos y de Etiquetado", 3, 8),
        Asignatura("TYBDLA", "Tecnología y Biotecnología de los Alimentos", 4, 8),
        Asignatura("NYSP", "Nutrición y Salud Pública", 4, 8),
        Asignatura("SN", "Socioantropología Nutricional", 3, 8),
        Asignatura("AYGDSAYN", "Administración y Gestión de Servicios de Alimentación y Nutrición", 4, 8),
        Asignatura("DYEDPN", "Diseño y Evaluación de Programas Nutricionales", 4, 8),
        Asignatura("AYGDAI", "Administración y Gestión de Alimentos Industriales", 4, 9),
        Asignatura("PP", "Práctica Profesional", 4, 9),
        Asignatura("CDE", "Culminación de Estudios", 4, 9),  
        ]
        for m in lista_nutricion:
            materias_nutricion[m.codigo] = m
            grafo_nutricion.agregar_materia(m.codigo)

        grafo_nutricion.agregar_relacion("A1CE", "A2CE")
        grafo_nutricion.agregar_relacion("A2CE", "A2+CE")
        grafo_nutricion.agregar_relacion("A2+CE", "B1CE")
        grafo_nutricion.agregar_relacion("B1CE", "B1+CE")
        grafo_nutricion.agregar_relacion("B1+CE", "B2CE")
        grafo_nutricion.agregar_relacion("CYL1", "CYL2")

        grafo_nutricion.agregar_relacion("MB", "B")
        grafo_nutricion.agregar_relacion("A", "NH1")
        grafo_nutricion.agregar_relacion("NH1", "NH2")
        grafo_nutricion.agregar_relacion("EDEL1", "EDEL2")
        grafo_nutricion.agregar_relacion("NH2", "IALD")
        grafo_nutricion.agregar_relacion("IALD", "DAINYA")
        grafo_nutricion.agregar_relacion("DAINYA", "DAYAM")
        grafo_nutricion.agregar_relacion("A", "FN1")
        grafo_nutricion.agregar_relacion("FN1", "FN2")
        grafo_nutricion.agregar_relacion("IALB", "MEHDLA")
        grafo_nutricion.agregar_relacion("MEHDLA", "TDLA")
        grafo_nutricion.agregar_relacion("AYGDSAYN", "AYGDAI")
        grafo_nutricion.agregar_relacion("MDLI", "CDE")
        
        self.carreras["Nutricion"] = {
            "materias": materias_nutricion,
            "grafo": grafo_nutricion
                        }

        materias_odontologia = {}
        grafo_odontologia = Grafo()

        lista_odontologia = [
        Asignatura("A1CE", "A1 Communicative English", 3, 1),
        Asignatura("CYL1", "Comunicación y Lenguaje I", 3, 1),
        Asignatura("IALO", "Introducción a la Odontología", 4, 1),
        Asignatura("AH1", "Anatomía Humana I", 4, 1),
        Asignatura("ES", "Educación Sanitaria", 3, 1),
        Asignatura("MB", "Matemática Básica", 4, 1),
        Asignatura("PIU", "Proyección e Integración Universitaria", 3, 1),
        Asignatura("INYOP", "Identidad Nacional y Orgullo Patrio", 3, 1),
        Asignatura("BIE", "Bioestadística", 4, 2),
        Asignatura("AH2", "Anatomía Humana II", 4, 2),
        Asignatura("BIO", "Biología", 4, 2),
        Asignatura("CYL2", "Comunicación y Lenguaje II", 3, 2),
        Asignatura("A2CE", "A2 Communicative English", 3, 2),
        Asignatura("FD", "Fotografía Digital", 3, 2),
        Asignatura("AD", "Anatomía Dental", 4, 2),
        Asignatura("HEIN", "Historia de Identidad Nacional", 3, 2),
        Asignatura("A2+CE", "A2+ Communicative English", 3, 3),
        Asignatura("MD1", "Materiales Dentales I", 4, 3),
        Asignatura("BQ", "Bioquímica", 4, 3),
        Asignatura("FH", "Fisiología Humana", 4, 3),
        Asignatura("HE", "Histoembriología", 4, 3),
        Asignatura("PEO", "Psicología en Odontología", 3, 3),
        Asignatura("EG", "Epidemiología", 3, 3),
        Asignatura("OP", "Odontología Preventiva", 4, 3),
        Asignatura("B1CE", "B1 Communicative English", 3, 4),
        Asignatura("MDLI", "Metodología de la Investigación", 4, 4),
        Asignatura("MD2", "Materiales Dentales II", 4, 4),
        Asignatura("SG", "Semiología", 4, 4),
        Asignatura("HB", "Histoembriología Bucodental", 4, 4),
        Asignatura("MO", "Microbiología Oral", 4, 4),
        Asignatura("O1", "Oclusión I", 4, 4),
        Asignatura("B1+CE", "B1+ Communicative English", 3, 5),
        Asignatura("AG", "Anestesiología", 4, 5),
        Asignatura("RG", "Radiología", 4, 5),
        Asignatura("PDOD", "Preclínica de Operatoria Dental", 4, 5),
        Asignatura("O2", "Oclusión II", 4, 5),
        Asignatura("FB", "Farmacología Básica", 4, 5),
        Asignatura("PG", "Patología General", 4, 5),
        Asignatura("OD", "Odontología Digital", 3, 5),
        Asignatura("B2CE", "B2 Communicative English", 3, 6),
        Asignatura("PO1", "Patología Oral I", 4, 6),
        Asignatura("OD1", "Operatoria Dental I", 4, 6),
        Asignatura("P1", "Periodoncia I", 4, 6),
        Asignatura("FO", "Farmacología Odontológica", 4, 6),
        Asignatura("CO1", "Cirugía Oral I", 4, 6),
        Asignatura("MO", "Medicina Oral", 4, 6),
        Asignatura("ES", "Emprendedores", 3, 7),
        Asignatura("PO2", "Patología Oral II", 4, 7),
        Asignatura("PDDPPF", "Preclínica de Prótesis Parcial Fija", 4, 7),
        Asignatura("P2", "Periodoncia II", 4, 7),
        Asignatura("CO2", "Cirugía Oral II", 4, 7),
        Asignatura("PDE", "Preclínica de Endodoncia", 4, 7),
        Asignatura("OD2", "Operatoria Dental II", 4, 7),
        Asignatura("PDO", "Preclínica de Odontopediatría", 4, 8),
        Asignatura("PDPDT", "Preclínica de Prótesis Total", 4, 8),
        Asignatura("PDDPPR", "Preclínica de Prótesis Parcial Removible", 4, 8),
        Asignatura("CM1", "Clínica Multidisciplinaria I", 4, 8),
        Asignatura("CO3", "Cirugía Oral III", 4, 8),
        Asignatura("CDO", "Clínica de Odontopediatría", 4, 9),
        Asignatura("CDPT", "Clínica de Prótesis Total", 4, 9),
        Asignatura("EA", "Educación Ambiental", 3, 9),
        Asignatura("CDPPR", "Clínica de Prótesis Parcial Removible", 4, 9),
        Asignatura("PDO", "Preclínica de Ortodoncia", 4, 9),
        Asignatura("CM2", "Clínica Multidisciplinaria II", 4, 9),
        Asignatura("CDO", "Clínica de Ortodoncia", 4, 10),
        Asignatura("AYMEO", "Administración y Mercadeo en Odontología", 3, 10),
        Asignatura("CM3", "Clínica Multidisciplinaria III", 4, 10),
        Asignatura("OLF", "Odontología Legal y Forense", 3, 10),
        Asignatura("FDE", "Formas de Culminación de Estudios", 4, 10),
        ]

        for m in lista_odontologia:
            materias_odontologia[m.codigo] = m
            grafo_odontologia.agregar_materia(m.codigo)

        grafo_odontologia.agregar_relacion("A1CE", "A2CE")
        grafo_odontologia.agregar_relacion("A2CE", "A2+CE")
        grafo_odontologia.agregar_relacion("A2+CE", "B1CE")
        grafo_odontologia.agregar_relacion("B1CE", "B1+CE")
        grafo_odontologia.agregar_relacion("B1+CE", "B2CE")
        grafo_odontologia.agregar_relacion("CYL1", "CYL2")

        grafo_odontologia.agregar_relacion("AH1", "AH2")
        grafo_odontologia.agregar_relacion("AH2", "AD")
        grafo_odontologia.agregar_relacion("BIO", "BQ")
        grafo_odontologia.agregar_relacion("HE", "HB")
        grafo_odontologia.agregar_relacion("MD1", "MD2")
        grafo_odontologia.agregar_relacion("O1", "O2")
        grafo_odontologia.agregar_relacion("FB", "FO")
        grafo_odontologia.agregar_relacion("PG", "PO1")
        grafo_odontologia.agregar_relacion("PO1", "PO2")
        grafo_odontologia.agregar_relacion("MO1", "MO2")

        grafo_odontologia.agregar_relacion("PDOD", "OD1")
        grafo_odontologia.agregar_relacion("OD1", "OD2")
        grafo_odontologia.agregar_relacion("P1", "P2")
        grafo_odontologia.agregar_relacion("CO1", "CO2")
        grafo_odontologia.agregar_relacion("CO2", "CO3")
        grafo_odontologia.agregar_relacion("PDOP", "CDOP")
        grafo_odontologia.agregar_relacion("PDOR", "CDOR")
        grafo_odontologia.agregar_relacion("PDPDT", "CDPT")
        grafo_odontologia.agregar_relacion("PDDPPR", "CDPPR")
        grafo_odontologia.agregar_relacion("CM1", "CM2")
        grafo_odontologia.agregar_relacion("CM2", "CM3")
        grafo_odontologia.agregar_relacion("MDLI", "FDE")

        self.carreras["Odontologia"] = {
            "materias": materias_odontologia,
            "grafo": grafo_odontologia
                        }

        materias_diplomacia = {}
        grafos_diplomacia = Grafo()

        lista_diplomacia = [
        Asignatura("EC2C", "Electiva Cultura 2 Créditos", 2, 1),
        Asignatura("ED2C", "Electiva Deporte 2 Créditos", 2, 1),
        Asignatura("IAEDD", "Introducción al Estudio del Derecho", 4, 1),
        Asignatura("EPS1", "Electiva Proyección Social I", 3, 1),
        Asignatura("EPS2", "Electiva Proyección Social II", 3, 1),
        Asignatura("A1CE", "A1 Communicative English", 3, 1),
        Asignatura("CYL1", "Comunicación y Lenguaje I", 3, 1),
        Asignatura("S", "Sociología", 4, 1),
        Asignatura("MB", "Matemática Básica", 4, 1),
        Asignatura("E1", "Electiva I", 3, 1),
        Asignatura("INYOP", "Identidad Nacional y Orgullo Patrio", 3, 1),
        Asignatura("EADF", "Electiva Actividades de Facultad", 3, 1),
        Asignatura("IALCP", "Introd. a la Ciencia Política", 4, 2),
        Asignatura("CPCS", "Cálculo para Ciencias Sociales", 4, 2),
        Asignatura("CYL2", "Comunicación y Lenguaje II", 3, 2),
        Asignatura("PDE", "Principios de Economía", 4, 2),
        Asignatura("A2CE", "A2 Communicative English", 3, 2),
        Asignatura("ED", "Estadística Descriptiva", 4, 2),
        Asignatura("HEIN", "Historia e Identidad Nacional", 3, 2),
        Asignatura("A2+CE", "A2+ Communicative English", 3, 3),
        Asignatura("FDMA", "Fundamentos de Microeconomía", 4, 3),
        Asignatura("HMYC", "Historia Moderna y Contemporánea", 3, 3),
        Asignatura("FP", "Filosofía Política", 4, 3),
        Asignatura("IALRI", "Introd. a las Relaciones Internacionales", 4, 3),
        Asignatura("ADM", "Análisis de Multivariables", 4, 3),
        Asignatura("B1CE", "B1 Communicative English", 3, 4),
        Asignatura("MDLI", "Metodología de la Investigación", 4, 4),
        Asignatura("FDM", "Fundamentos de Macroeconomía", 4, 4),
        Asignatura("EDLCS", "Epistemología de las Ciencias Sociales", 4, 4),
        Asignatura("HDNYAAL", "Historia de Nicaragua y América Latina", 3, 4),
        Asignatura("DIP1", "Derecho Internacional Público I", 4, 4),
        Asignatura("B1+CE", "B1+ Communicative English", 3, 5),
        Asignatura("GP", "Geografía Política", 3, 5),
        Asignatura("DIP2", "Derecho Internacional Público II", 4, 5),
        Asignatura("LP", "Legislación Pública", 4, 5),
        Asignatura("SPC", "Sistemas Políticos Comparados", 4, 5),
        Asignatura("E2", "Electiva II", 3, 5),
        Asignatura("NYPP", "Normas y Procedimientos Protocolarios", 3, 6),
        Asignatura("IALTDJ", "Introducción a la Teoría de Juegos", 4, 6),
        Asignatura("CI", "Comercio Internacional", 4, 6),
        Asignatura("B2CE", "B2 Communicative English", 3, 6),
        Asignatura("E3", "Electiva III", 3, 6),
        Asignatura("E", "Emprendedores", 3, 7),
        Asignatura("SDDI", "Seminario en Derecho Internacional", 4, 7),
        Asignatura("REI1", "Relaciones Económicas Internacionales I", 4, 7),
        Asignatura("OI1", "Organizaciones Internacionales I", 4, 7),
        Asignatura("PEDNYC1", "Política Exterior de Nicaragua y Centroamérica I", 4, 7),
        Asignatura("I7PDRYRI", "Inglés VII para Diplomacia y Relaciones Internacionales", 3, 7),
        Asignatura("I8PDRYRI", "Inglés VIII para Diplomacia y Relaciones Internacionales", 3, 8),
        Asignatura("FDPP", "Formulación de Políticas Públicas", 4, 8),
        Asignatura("REI2", "Relaciones Económicas Internacionales II", 4, 8),
        Asignatura("PEDNYC2", "Política Exterior de Nicaragua y Centroamérica II", 4, 8),
        Asignatura("CAD", "Cooperación al Desarrollo", 3, 8),
        Asignatura("OI2", "Organismos Internacionales II", 4, 8),
        Asignatura("ADPP", "Análisis de Políticas Públicas", 4, 9),
        Asignatura("TYPRDC", "Teoría y Práctica de Resolución de Conflictos", 4, 9),
        Asignatura("IC", "Integración Centroamericana", 4, 9),
        Asignatura("GPU", "Gestión Pública", 4, 9),
        Asignatura("PP", "Prácticas Profesionales", 4, 9),
        Asignatura("SDEI", "Seminario en Economía Internacional", 4, 9),
        Asignatura("PYDEAAL", "Pobreza y Desarrollo en América Latina", 3, 10),
        Asignatura("SESYDN", "Seminario en Seguridad y Defensa Nacional", 4, 10),
        Asignatura("TYPDLN", "Teoría y Práctica de la Negociación", 4, 10),
        Asignatura("FYEDP", "Formulación y Evaluación de Proyectos", 4, 10),
        Asignatura("TYPDYC", "Teoría y Práctica Diplomática y Consular", 4, 10),
        Asignatura("ECDE", "Electiva Culminación de Estudios", 4, 10),
        ]

        for m in lista_diplomacia:
            materias_diplomacia[m.codigo] = m
            grafos_diplomacia.agregar_materia(m.codigo)

        grafos_diplomacia.agregar_relacion("A1CE", "A2CE")
        grafos_diplomacia.agregar_relacion("A2CE", "A2+CE")
        grafos_diplomacia.agregar_relacion("A2+CE", "B1CE")
        grafos_diplomacia.agregar_relacion("B1CE", "B1+CE")
        grafos_diplomacia.agregar_relacion("B1+CE", "B2CE")
        grafos_diplomacia.agregar_relacion("B2CE", "I7PDRYRI")
        grafos_diplomacia.agregar_relacion("I7PDRYRI", "I8PDRYRI")
        grafos_diplomacia.agregar_relacion("CYL1", "CYL2")

        grafos_diplomacia.agregar_relacion("MB", "CPCS")
        grafos_diplomacia.agregar_relacion("ED", "ADM")
        grafos_diplomacia.agregar_relacion("PDE", "FDMA")
        grafos_diplomacia.agregar_relacion("FDMA", "FDM")
        grafos_diplomacia.agregar_relacion("IAEDD", "DIP1")
        grafos_diplomacia.agregar_relacion("DIP1", "DIP2")
        grafos_diplomacia.agregar_relacion("DIP2", "SDDI")
        grafos_diplomacia.agregar_relacion("IALRI", "REI1")
        grafos_diplomacia.agregar_relacion("REI1", "REI2")
        grafos_diplomacia.agregar_relacion("REI2", "SDEI")
        grafos_diplomacia.agregar_relacion("IALRI", "OI1")
        grafos_diplomacia.agregar_relacion("OI1", "OI2")
        grafos_diplomacia.agregar_relacion("PEDNYC1", "PEDNYC2")
        grafos_diplomacia.agregar_relacion("FDPP", "ADPP")
        grafos_diplomacia.agregar_relacion("GP", "GPU")
        grafos_diplomacia.agregar_relacion("MDLI", "ECDE")

        self.carreras["Diplomacia y Relaciones Internacionales"] = {
            "materias": materias_diplomacia,
            "grafo": grafos_diplomacia
                        }

        carreras_marketing = {}
        grafo_marketing = Grafo()

        lista_marketing = [
    Asignatura("PDA", "Principios de Administración", 4, 1),
        Asignatura("MB", "Matemática Básica", 4, 1),
        Asignatura("CYL1", "Comunicación y Lenguaje I", 3, 1),
        Asignatura("FDM", "Fundamentos de Marketing", 4, 1),
        Asignatura("TDLCP", "Teoría de la Comunicación Publicitaria", 4, 1),
        Asignatura("A1CE", "A1 Communicative English", 3, 1),
        Asignatura("PIU", "Proyección e Integración Universitaria", 3, 1),
        Asignatura("INYOP", "Identidad Nacional y Orgullo Patrio", 3, 1),
        Asignatura("CDC", "Comportamiento del Consumidor", 4, 2),
        Asignatura("E1", "Estadística I", 4, 2),
        Asignatura("EA", "Educación Ambiental", 3, 2),
        Asignatura("RP", "Redacción Publicitaria", 4, 2),
        Asignatura("CYL2", "Comunicación y Lenguaje II", 3, 2),
        Asignatura("HEIN", "Historia e Identidad Nacional", 3, 2),
        Asignatura("A2CE", "A2 Communicative English", 3, 2),
        Asignatura("C1", "Contabilidad I", 4, 2),
        Asignatura("MLDMYP", "Marco Legal del Marketing y Publicidad", 3, 3),
        Asignatura("PDE", "Principios de Economía", 4, 3),
        Asignatura("A2+CE", "A2+ Communicative English", 3, 3),
        Asignatura("CDC1", "Contabilidad de Costos I", 4, 3),
        Asignatura("EDP", "Estrategia de Producto", 4, 3),
        Asignatura("FDDD", "Fundamentos del Diseño Digital", 3, 3),
        Asignatura("TDOYN", "Técnicas de Oratoria y Negociación", 3, 3),
        Asignatura("MDS", "Marketing de Servicios", 4, 4),
        Asignatura("DE1", "Derecho Empresarial I", 3, 4),
        Asignatura("F1", "Finanzas I", 4, 4),
        Asignatura("B1CE", "B1 Communicative English", 3, 4),
        Asignatura("EDPYR", "Estrategia de Precios y Rentabilidad", 4, 4),
        Asignatura("IDM", "Investigación de Mercado", 4, 4),
        Asignatura("FF", "Fotografía Fundamental", 3, 4),
        Asignatura("MYCP", "Marketing y Comunicación Política", 3, 5),
        Asignatura("CPTYD", "Comunicación Publicitaria: Tradicional y Digital", 4, 5),
        Asignatura("B1+CE", "B1+ Communicative English", 3, 5),
        Asignatura("EDDYC", "Estrategia de Distribución y Comercialización", 4, 5),
        Asignatura("P", "Presupuesto", 4, 5),
        Asignatura("MSV", "Marketing Social Verde", 3, 5),
        Asignatura("O1", "Optativa I", 3, 6),
        Asignatura("PEP", "Producción Estratégica Publicitaria", 4, 6),
        Asignatura("MDI", "Metodología de Investigación", 4, 6),
        Asignatura("BM", "Brand Management", 4, 6),
        Asignatura("MA", "Marketing Analítico", 4, 6),
        Asignatura("B2CE", "B2 Communicative English", 3, 6),
        Asignatura("O2", "Optativa II", 3, 7),
        Asignatura("E", "Emprendedores", 3, 7),
        Asignatura("N", "Neuromarketing", 4, 7),
        Asignatura("BI", "Business Intelligence", 4, 7),
        Asignatura("TMYM", "Trade Marketing y Merchandising", 4, 7),
        Asignatura("PCYTDD", "Pensamiento Crítico y Toma de Decisiones", 3, 7),
        Asignatura("CS", "Corporate Strategy", 4, 8),
        Asignatura("CRM", "Customer Relationship Management (CRM)", 4, 8),
        Asignatura("HRM", "Human Resources Management", 3, 8),
        Asignatura("SM", "Sales Management", 4, 8),
        Asignatura("MD", "Marketing Digital", 4, 8),
        Asignatura("CI", "Comercio Internacional", 4, 8),
        Asignatura("MI", "Marketing Internacional", 4, 9),
        Asignatura("TDIAYNTEP", "Taller de Inteligencia Artificial y Nuevas Tendencias en Publicidad", 4, 9),
        Asignatura("DDM", "Dirección de Marketing", 4, 9),
        Asignatura("PP", "Prácticas Profesionales", 4, 9),
        Asignatura("FDE", "Formas de Culminación de Estudios", 4, 9),
        ]

        for m in lista_marketing:
            carreras_marketing[m.codigo] = m
            grafo_marketing.agregar_materia(m.codigo)

        grafo_marketing.agregar_relacion("A1CE", "A2CE")
        grafo_marketing.agregar_relacion("A2CE", "A2+CE")
        grafo_marketing.agregar_relacion("A2+CE", "B1CE")
        grafo_marketing.agregar_relacion("B1CE", "B1+CE")
        grafo_marketing.agregar_relacion("B1+CE", "B2CE")
        grafo_marketing.agregar_relacion("CYL1", "CYL2")    

        grafo_marketing.agregar_relacion("FDM", "CDC")
        grafo_marketing.agregar_relacion("FDM", "EDP")
        grafo_marketing.agregar_relacion("EDP", "EDPYR")
        grafo_marketing.agregar_relacion("EDP", "EDDYC")
        grafo_marketing.agregar_relacion("FDM", "BM")
        grafo_marketing.agregar_relacion("BM", "DDM")
        grafo_marketing.agregar_relacion("TDLCP", "RP")
        grafo_marketing.agregar_relacion("RP", "CPTYD")
        grafo_marketing.agregar_relacion("CPTYD", "PEP")
        grafo_marketing.agregar_relacion("PEP", "TDIAYNTEP")
        grafo_marketing.agregar_relacion("C1", "CDC1")
        grafo_marketing.agregar_relacion("CDC1", "F1")
        grafo_marketing.agregar_relacion("F1", "P")
        grafo_marketing.agregar_relacion("E1", "IDM")
        grafo_marketing.agregar_relacion("IDM", "MA")
        grafo_marketing.agregar_relacion("CI", "MI")
        grafo_marketing.agregar_relacion("MDI", "FDE")

        self.carreras["Marketing y Publicidad"] = {
            "materias": carreras_marketing,
            "grafo": grafo_marketing
                        }

        carreras_diseño = {}
        grafo_diseño = Grafo()

        lista_diseño = [
        Asignatura("FDLC", "Fundamentos de la Composición", 4, 1),
        Asignatura("FDLC2", "Fundamentos de la Creatividad", 4, 1),
        Asignatura("B", "Bocetos", 4, 1),
        Asignatura("PIU", "Proyección e Integración Universitaria", 3, 1),
        Asignatura("CYL1", "Comunicación y Lenguaje I", 3, 1),
        Asignatura("A1CE1", "A1 Communicative English I", 3, 1),
        Asignatura("MB", "Matemática Básica", 4, 1),
        Asignatura("INYOP", "Identidad Nacional y Orgullo Patrio", 3, 1),
        Asignatura("DNYA", "Dibujo Natural y Anatómico", 4, 2),
        Asignatura("TDEG", "Técnicas de Expresión Gráfica", 4, 2),
        Asignatura("TYPDC", "Teoría y Psicología del Color", 4, 2),
        Asignatura("DV", "Diseño Vectorial", 4, 2),
        Asignatura("HEIN", "Historia e Identidad Nacional", 3, 2),
        Asignatura("A2CE2", "A2 Communicative English II", 3, 2),
        Asignatura("CYL2", "Comunicación y Lenguaje II", 3, 2),
        Asignatura("DT", "Dibujo Técnico", 4, 3),
        Asignatura("HEIDA", "Historia e Interpretación del arte", 3, 3),
        Asignatura("T", "Tipografía", 4, 3),
        Asignatura("TDI", "Taller de Ilustración", 4, 3),
        Asignatura("PC", "Pensamiento Creativo", 3, 3),
        Asignatura("IC", "Imagen Creativa", 4, 3),
        Asignatura("A2+CE3", "A2 + Communicative English III", 3, 3),
        Asignatura("PG", "Productos Gráficos", 4, 4),
        Asignatura("FF", "Fotografía Fundamental", 4, 4),
        Asignatura("PDD", "Procesos del Diseño", 4, 4),
        Asignatura("HDD", "Historia del Diseño", 3, 4),
        Asignatura("DD", "Diagramación Digital", 4, 4),
        Asignatura("B2CE4", "B2 Communicative English IV", 3, 4),
        Asignatura("EA", "Educación Ambiental", 3, 4),
        Asignatura("PA1", "Producción Audiovisual I", 4, 5),
        Asignatura("PDI", "Procesos de Impresión", 4, 5),
        Asignatura("TDLCP", "Teorías de la comunicación publicitaria", 3, 5),
        Asignatura("FP", "Fotografía Publicitaria", 4, 5),
        Asignatura("IVYB", "Identidad Visual y Branding", 4, 5),
        Asignatura("E1", "Estadísticas I", 4, 5),
        Asignatura("B1+CE5", "B1 + Communicative English V", 3, 5),
        Asignatura("PA2", "Producción Audiovisual II", 4, 6),
        Asignatura("DDAYF", "Dirección de Arte y Fotografía", 4, 6),
        Asignatura("TDPDA", "Taller de Producción de Audio", 4, 6),
        Asignatura("NPD", "Negocios para Diseñadores", 3, 6),
        Asignatura("M3D", "Modelado 3D", 4, 6),
        Asignatura("MDLI", "Metodología de la Investigación", 4, 6),
        Asignatura("B2CE6", "B2 Communicative English VI", 3, 6),
        Asignatura("TPC", "Taller Producción Cinematográfica", 4, 7),
        Asignatura("PCYTDD", "Pensamiento crítico y toma de decisiones", 3, 7),
        Asignatura("RP", "Redacción Publicitaria", 3, 7),
        Asignatura("FDM", "Fundamentos del Marketing", 3, 7),
        Asignatura("PDE", "Producción de Eventos", 3, 7),
        Asignatura("A3DB", "Animación 3D (blender)", 4, 7),
        Asignatura("PPA", "Post producción Audiovisual", 4, 7),
        Asignatura("CDCYP", "Campaña de Comunicación y Publicidad", 4, 8),
        Asignatura("IDM", "Investigación de Mercado", 4, 8),
        Asignatura("MD", "Marketing Digital", 4, 8),
        Asignatura("PI", "Propiedad Intelectual", 3, 8),
        Asignatura("O1", "Optativa I", 3, 8),
        Asignatura("PP", "Prácticas Profesionales", 4, 8),
        Asignatura("O2", "Optativa II", 3, 9),
        Asignatura("E", "Emprendedores", 3, 9),
        Asignatura("FDE", "Forma de Culminación de Estudios", 4, 9),
        ]

        for m in lista_diseño:
            carreras_diseño[m.codigo] = m
            grafo_diseño.agregar_materia(m.codigo)

        grafo_diseño.agregar_relacion("A1CE1", "A2CE2")
        grafo_diseño.agregar_relacion("A2CE2", "A2+CE3")
        grafo_diseño.agregar_relacion("A2+CE3", "B2CE4")
        grafo_diseño.agregar_relacion("B2CE4", "B1+CE5")
        grafo_diseño.agregar_relacion("B1+CE5", "B2CE6")
        grafo_diseño.agregar_relacion("CYL1", "CYL2")

        grafo_diseño.agregar_relacion("B", "DNYA")
        grafo_diseño.agregar_relacion("FDLC", "DV")
        grafo_diseño.agregar_relacion("DV", "T")
        grafo_diseño.agregar_relacion("DV", "PG")
        grafo_diseño.agregar_relacion("PG", "DD")
        grafo_diseño.agregar_relacion("DD", "PDI")
        grafo_diseño.agregar_relacion("DD", "IVYB")
        grafo_diseño.agregar_relacion("FF", "FP")
        grafo_diseño.agregar_relacion("FP", "DDAYF")
        grafo_diseño.agregar_relacion("PA1", "PA2")
        grafo_diseño.agregar_relacion("PA2", "TPC")
        grafo_diseño.agregar_relacion("TPC", "PPA")
        grafo_diseño.agregar_relacion("M3D", "A3DB")
        grafo_diseño.agregar_relacion("MDLI", "FDE")
        
        self.carreras["Diseño y Comunicacion Visual"] = {
            "materias": carreras_diseño,
            "grafo": grafo_diseño
        }

        carreras_comunicacion = {}
        grafo_comunicacion = Grafo()

        lista_comunicacion = [
        Asignatura("CYL1", "Comunicación y Lenguaje I", 3, 1),
        Asignatura("A1CE", "A1 Communicative English", 3, 1),
        Asignatura("HEIN", "Historia e Identidad Nacional", 3, 1),
        Asignatura("PIU", "Proyección e Integración Universitaria", 3, 1),
        Asignatura("FDLCYLRRPP", "Fundamentos de la Comunicación y las RR.PP.", 4, 1),
        Asignatura("TDLC", "Teorías de la Comunicación", 4, 1),
        Asignatura("INYOP", "Identidad Nacional y Orgullo Patrio", 3, 1),
        Asignatura("EA", "Educación Ambiental", 3, 2),
        Asignatura("CYL2", "Comunicación y Lenguaje II", 3, 2),
        Asignatura("A2CE", "A2 Communicative English", 3, 2),
        Asignatura("LDLC", "Legislación de la Comunicación", 3, 2),
        Asignatura("ISYC", "Innovación Social y Comunicación", 4, 2),
        Asignatura("ADD", "Análisis del Discurso", 4, 2),
        Asignatura("PC", "Pensamiento Creativo", 3, 2),
        Asignatura("A2+CE", "A2+ Communicative English", 3, 3),
        Asignatura("CIYCO", "Comunicación Interna y Clima Organizacional", 4, 3),
        Asignatura("RPYMP", "Relaciones Públicas y Mix Promocional", 4, 3),
        Asignatura("MYT", "Medios y TIC's", 4, 3),
        Asignatura("TDPD", "Taller de Producción Digital", 4, 3),
        Asignatura("AMYEDD", "Análisis Matemático y Estadística de Datos", 4, 3),
        Asignatura("PCYTDD", "Pensamiento Crítico y Toma de Decisiones", 3, 3),
        Asignatura("B1CE", "B1 Communicative English", 3, 4),
        Asignatura("CE", "Comunicación Externa", 4, 4),
        Asignatura("NYCDC", "Neurocomunicación y Cambio de Conducta", 4, 4),
        Asignatura("PEDLRRPP", "Planificación Estratégica de las RR.PP.", 4, 4),
        Asignatura("CEI", "Contenido e Imagen", 4, 4),
        Asignatura("TDEDYD", "Taller de Edición, Diseño y Diagramación", 4, 4),
        Asignatura("OYCP", "Oratoria y Comunicación Persuasiva", 3, 4),
        Asignatura("INYOP2", "Identidad Nacional y Orgullo Patrio", 3, 4),
        Asignatura("B1+CE", "B1+ Communicative English", 3, 5),
        Asignatura("BM", "Brand Management", 4, 5),
        Asignatura("TDPDA", "Taller de Producción de Audio", 4, 5),
        Asignatura("PSYSYAW", "Posicionamiento SEO y SEM y Analítica Web", 4, 5),
        Asignatura("CYPE", "Comunicación y Producción Editorial", 4, 5),
        Asignatura("IEIC", "Identidad e Imagen Corporativa", 4, 5),
        Asignatura("TDR", "Taller de Redacción", 3, 5),
        Asignatura("B2CE", "B2 Communicative English", 3, 6),
        Asignatura("LYGDLC", "Lobbying y Gestión de la Comunicación", 4, 6),
        Asignatura("TDV", "Taller de Vocería", 3, 6),
        Asignatura("S", "Storytelling", 4, 6),
        Asignatura("PA", "Producción Audiovisual", 4, 6),
        Asignatura("RESYC", "Redacción Estratégica, Stakeholders y Canales", 4, 6),
        Asignatura("ADC", "Análisis de Costos", 3, 6),
        Asignatura("GYSDCC", "Gestión y solución de crisis comunicacionales", 4, 7),
        Asignatura("DYEDC", "Diseño y Estrategias de Campañas", 4, 7),
        Asignatura("PA2", "Postproducción Audiovisual", 4, 7),
        Asignatura("MDLI", "Metodología de la Investigación", 4, 7),
        Asignatura("O1", "Optativa I", 3, 7),
        Asignatura("E", "Emprendedores", 3, 8),
        Asignatura("PP", "Prácticas Profesionales", 4, 8),
        Asignatura("TDPC", "Taller de Producción Cinematográfica", 4, 8),
        Asignatura("GDEYP", "Gestión de Eventos y Protocolo", 3, 8),
        Asignatura("TDIENCE", "Taller de Innovación en Comunicación Estratégica", 4, 9),
        Asignatura("GDIYRPPD", "Gestión de Imagen y Reputación en Plataformas Digitales", 4, 9),
        Asignatura("FDCDE", "Formas de Culminación de Estudios", 4, 9),
        ]

        for m in lista_comunicacion:
            carreras_comunicacion[m.codigo] = m
            grafo_comunicacion.agregar_materia(m.codigo)

        grafo_comunicacion.agregar_relacion("A1CE", "A2CE")
        grafo_comunicacion.agregar_relacion("A2CE", "A2+CE")
        grafo_comunicacion.agregar_relacion("A2+CE", "B1CE")
        grafo_comunicacion.agregar_relacion("B1CE", "B1+CE")
        grafo_comunicacion.agregar_relacion("B1+CE", "B2CE")
        grafo_comunicacion.agregar_relacion("CYL1", "CYL2")

        grafo_comunicacion.agregar_relacion("TDLC", "ADD")
        grafo_comunicacion.agregar_relacion("FDLCYLRRPP", "CIYCO")
        grafo_comunicacion.agregar_relacion("FDLCYLRRPP", "RPYMP")
        grafo_comunicacion.agregar_relacion("RPYMP", "PEDLRRPP")
        grafo_comunicacion.agregar_relacion("PEDLRRPP", "LYGDLC")
        grafo_comunicacion.agregar_relacion("LYGDLC", "GYSDCC")
        grafo_comunicacion.agregar_relacion("TDPD", "TDEDYD")
        grafo_comunicacion.agregar_relacion("TDEDYD", "CYPE")
        grafo_comunicacion.agregar_relacion("PA", "PA2")
        grafo_comunicacion.agregar_relacion("PA2", "TDPC")
        grafo_comunicacion.agregar_relacion("BM", "IEIC")
        grafo_comunicacion.agregar_relacion("MDLI", "FDCDE")

    
        self.carreras["Comunicacion y Relaciones Publicas"] = {
            "materias": carreras_comunicacion,
            "grafo": grafo_comunicacion
        }

        carreras_administracion = {}
        grafo_administracion = Grafo()

        lista_administracion = [
        Asignatura("IC1", "Inglés Comunicativo I", 3, 1),
        Asignatura("CYL1", "Comunicación y Lenguaje I", 3, 1),
        Asignatura("MB", "Matemática Básica", 4, 1),
        Asignatura("ECI1Y2", "Electiva Cultura I y II", 3, 1),
        Asignatura("EDI1Y2", "Electiva Deporte I y II", 3, 1),
        Asignatura("OPN", "Ofimática para los Negocios", 3, 1),
        Asignatura("EAALN", "Estadísticas Aplicadas a los Negocios", 4, 1),
        Asignatura("TDTDA", "Teoría General de la Administración", 4, 1),
        Asignatura("IC2", "Inglés Comunicativo II", 3, 2),
        Asignatura("CYL2", "Comunicación y Lenguaje II", 3, 2),
        Asignatura("EPS1Y2", "Electiva Proyección Social I y II", 3, 2),
        Asignatura("EADF", "Electiva Actividades de Facultad", 3, 2),
        Asignatura("DMA", "Derecho Mercantil y Aduanero", 3, 2),
        Asignatura("MDLIAPN", "Metodología de la Investigación para Negocios", 4, 2),
        Asignatura("CF", "Contabilidad Financiera", 4, 2),
        Asignatura("AO", "Arquitectura Organizacional", 4, 2),
        Asignatura("IC3", "Inglés Comunicativo III", 3, 3),
        Asignatura("DLYS", "Derecho Laboral y Seguridad Social", 3, 3),
        Asignatura("CDC", "Contabilidad de Costos", 4, 3),
        Asignatura("PDE", "Principios de Economía", 4, 3),
        Asignatura("GDTH", "Gestión del Talento Humano", 3, 3),
        Asignatura("FDM", "Fundamentos de Marketing", 4, 3),
        Asignatura("ACPLG", "Análisis Cuantitativo para la Gestión", 4, 3),
        Asignatura("IC4", "Inglés Comunicativo IV", 3, 4),
        Asignatura("CO", "Comportamiento Organizacional", 3, 4),
        Asignatura("IDM", "Investigación de Mercado", 4, 4),
        Asignatura("GDLCDS", "Gestión de la Cadena de Suministro", 4, 4),
        Asignatura("F1", "Finanzas I", 4, 4),
        Asignatura("GC", "Gobierno Corporativo", 3, 4),
        Asignatura("TDLCP", "Teoría de la Comunicación Publicitaria", 3, 4),
        Asignatura("EDPYR", "Estrategia de Precios y Rentabilidad", 4, 4),
        Asignatura("IC5", "Inglés Comunicativo V", 3, 5),
        Asignatura("CDSAC", "Cultura de Servicio al Cliente", 3, 5),
        Asignatura("IDN", "Inteligencia de Negocios", 4, 5),
        Asignatura("HG", "Habilidades Gerenciales", 3, 5),
        Asignatura("GDPYSGC", "Gestión de Procesos y SGC", 4, 5),
        Asignatura("F2", "Finanzas II", 4, 5),
        Asignatura("IC6", "Inglés Comunicativo VI", 3, 6),
        Asignatura("AFDLO", "Administración Fiscal de la Organización", 4, 6),
        Asignatura("AELDLDE", "Análisis Estratégico de la Empresa", 4, 6),
        Asignatura("RSE", "Responsabilidad Social Empresarial", 3, 6),
        Asignatura("IYDT", "Innovación y Design Thinking", 3, 6),
        Asignatura("MBU", "Mercado Bursátiles", 4, 6),
        Asignatura("RSYME", "Redes sociales y Marketing Electrónico", 4, 6),
        Asignatura("ADLRDLC", "Administración de las Relaciones con los clientes", 4, 6),
        Asignatura("E", "Emprendedores", 3, 7),
        Asignatura("EF", "Empresas Familiares", 3, 7),
        Asignatura("CS", "Corporate Strategy", 4, 7),
        Asignatura("FS", "Financial Strategy", 4, 7),
        Asignatura("CDG", "Control de Gestión", 4, 8),
        Asignatura("PO", "Planeación Operativa", 4, 8),
        Asignatura("PP", "Prácticas Profesionales", 4, 8),
        Asignatura("BRM", "Business Risk Management", 4, 8),
        Asignatura("E1", "Electiva I", 3, 8),
        Asignatura("FI", "Finanzas Internacionales", 4, 8),
        Asignatura("SM", "Sales Management", 4, 8),
        Asignatura("LI", "Logística internacional", 4, 8),
        ]

        for m in lista_administracion:
            carreras_administracion[m.codigo] = m
            grafo_administracion.agregar_materia(m.codigo)

        grafo_administracion.agregar_relacion("IC1", "IC2")
        grafo_administracion.agregar_relacion("IC2", "IC3")
        grafo_administracion.agregar_relacion("IC3", "IC4")
        grafo_administracion.agregar_relacion("IC4", "IC5")
        grafo_administracion.agregar_relacion("IC5", "IC6")
        grafo_administracion.agregar_relacion("CYL1", "CYL2")

        grafo_administracion.agregar_relacion("TDTDA", "AO")
        grafo_administracion.agregar_relacion("AO", "CO")
        grafo_administracion.agregar_relacion("AO", "GC")
        grafo_administracion.agregar_relacion("AO", "GDPYSGC")
        grafo_administracion.agregar_relacion("GDPYSGC", "AELDLDE")
        grafo_administracion.agregar_relacion("AELDLDE", "CS")
        grafo_administracion.agregar_relacion("CS", "CDG")
        grafo_administracion.agregar_relacion("CF", "CDC")
        grafo_administracion.agregar_relacion("CDC", "F1")
        grafo_administracion.agregar_relacion("F1", "F2")
        grafo_administracion.agregar_relacion("F2", "FS")
        grafo_administracion.agregar_relacion("FS", "FI")
        grafo_administracion.agregar_relacion("FDM", "IDM")
        grafo_administracion.agregar_relacion("IDM", "EDPYR")
        grafo_administracion.agregar_relacion("MB", "ACPLG")

        self.carreras["Administracion de Empresas"] = {
            "materias": carreras_administracion,
            "grafo": grafo_administracion
        }

        carreras_contabilidad = {}
        grafo_contabilidad = Grafo()

        lista_contabilidad = [
        Asignatura("COM101", "Comunicación y Lenguaje I", 3, 1),
        Asignatura("PIU102", "Proyección e Integración Universitaria", 3, 1),
        Asignatura("ING103", "A1 Communicative English", 3, 1),
        Asignatura("CON104", "Contabilidad I", 4, 1),
        Asignatura("MAT105", "Matemática Básica", 4, 1),
        Asignatura("IDN106", "Identidad Nacional y Orgullo Patrio", 3, 1),
        Asignatura("ADM107", "Principios de Administración", 4, 1),
        Asignatura("CON201", "Contabilidad II", 4, 2),
        Asignatura("CAL202", "Cálculo I", 4, 2),
        Asignatura("HIS203", "Historia e Identidad Nacional", 3, 2),
        Asignatura("ING204", "A2 Communicative English", 3, 2),
        Asignatura("COM205", "Comunicación y Lenguaje II", 3, 2),
        Asignatura("EST206", "Estadística I", 4, 2),
        Asignatura("ING301", "A2+ Communicative English", 3, 3),
        Asignatura("AMB302", "Educación Ambiental", 3, 3),
        Asignatura("COS303", "Contabilidad de Costos I", 4, 3),
        Asignatura("CON304", "Contabilidad III", 4, 3),
        Asignatura("EST305", "Estadística II", 4, 3),
        Asignatura("MAF306", "Matemática Financiera", 4, 3),
        Asignatura("COS401", "Contabilidad de Costos II", 4, 4),
        Asignatura("ECO402", "Principios de Economía", 4, 4),
        Asignatura("ING403", "B1 Communicative English", 3, 4),
        Asignatura("DER404", "Derecho Empresarial I", 3, 4),
        Asignatura("FIN405", "Finanzas I", 4, 4),
        Asignatura("CON406", "Contabilidad IV", 4, 4),
        Asignatura("ING501", "B1+ Communicative English", 3, 5),
        Asignatura("SIC502", "Sistemas de Información Contable", 4, 5),
        Asignatura("FIN503", "Finanzas II", 4, 5),
        Asignatura("CBS504", "Contabilidad Bancaria y de Seguros", 4, 5),
        Asignatura("PLO505", "Planeación Operativa", 3, 5),
        Asignatura("DET506", "Derecho Tributario", 4, 5),
        Asignatura("AUD601", "Auditoría I", 4, 6),
        Asignatura("MBU602", "Mercados Bursátiles", 4, 6),
        Asignatura("COF603", "Contabilidad Fiscal", 4, 6),
        Asignatura("ING604", "B2 Communicative English", 3, 6),
        Asignatura("MET605", "Metodología de la Investigación", 4, 6),
        Asignatura("COA606", "Contabilidad Agropecuaria", 4, 6),
        Asignatura("AUD701", "Auditoría II", 4, 7),
        Asignatura("FII702", "Finanzas Internacionales", 4, 7),
        Asignatura("BRM703", "Business Risk Management", 4, 7),
        Asignatura("RSO704", "Responsabilidad Social", 3, 7),
        Asignatura("ESE705", "Estrategia Empresarial I", 4, 7),
        Asignatura("ETI706", "Ética Empresarial", 3, 7),
        Asignatura("ESE801", "Estrategia Empresarial II", 4, 8),
        Asignatura("AUS802", "Auditoría de Sistemas", 4, 8),
        Asignatura("HRM803", "Human Resources Management", 3, 8),
        Asignatura("FYA804", "Fusiones y Adquisiciones", 4, 8),
        Asignatura("FIN805", "Fintech", 3, 8),
        Asignatura("GOP806", "Gestión de Operaciones", 4, 8),
        Asignatura("FST1101", "Financial Strategy", 4, 11),
        Asignatura("AIO1102", "Auditoría Interna y Operacional", 4, 11),
        Asignatura("EMP1103", "Emprendedores", 3, 11),
        Asignatura("BLK1104", "Blockchain", 3, 11),
        Asignatura("FVS1105", "Finanzas Verdes y Sostenibles", 3, 11),
        Asignatura("PRP1201", "Prácticas Profesionales", 4, 12),
        Asignatura("FCE1202", "Formas de Culminación de Estudio", 4, 12),
        Asignatura("EAF1203", "Electiva Actividades de Facultad", 3, 12),
        ]

        for m in lista_contabilidad:
            carreras_contabilidad[m.codigo] = m
            grafo_contabilidad.agregar_materia(m.codigo)

        grafo_contabilidad.agregar_relacion("ING103", "ING204")
        grafo_contabilidad.agregar_relacion("ING204", "ING301")
        grafo_contabilidad.agregar_relacion("ING301", "ING403")
        grafo_contabilidad.agregar_relacion("ING403", "ING501")
        grafo_contabilidad.agregar_relacion("ING501", "ING604")
        grafo_contabilidad.agregar_relacion("COM101", "COM205")

        grafo_contabilidad.agregar_relacion("CON104", "CON201")
        grafo_contabilidad.agregar_relacion("CON201", "CON304")
        grafo_contabilidad.agregar_relacion("CON304", "CON406")
        grafo_contabilidad.agregar_relacion("CON406", "SIC502")
        grafo_contabilidad.agregar_relacion("CON406", "CBS504")
        grafo_contabilidad.agregar_relacion("CON406", "COA606")
        grafo_contabilidad.agregar_relacion("CON201", "COS303")
        grafo_contabilidad.agregar_relacion("COS303", "COS401")
        grafo_contabilidad.agregar_relacion("CON406", "AUD601")
        grafo_contabilidad.agregar_relacion("AUD601", "AUD701")
        grafo_contabilidad.agregar_relacion("AUD701", "AUS802")
        grafo_contabilidad.agregar_relacion("AUS802", "AIO1102")
        grafo_contabilidad.agregar_relacion("MAT105", "CAL202")
        grafo_contabilidad.agregar_relacion("MAT105", "MAF306")
        grafo_contabilidad.agregar_relacion("MAF306", "FIN405")
        grafo_contabilidad.agregar_relacion("FIN405", "FIN503")
        grafo_contabilidad.agregar_relacion("FIN503", "FII702")
        grafo_contabilidad.agregar_relacion("FII702", "FST1101")
        grafo_contabilidad.agregar_relacion("EST206", "EST305")
        grafo_contabilidad.agregar_relacion("ESE705", "ESE801")
        grafo_contabilidad.agregar_relacion("MET605", "FCE1202")

        self.carreras["Contabilidad y Finanzas"] = {
            "materias": carreras_contabilidad,
            "grafo": grafo_contabilidad
        }

        carreras_economia = {}
        grafo_economia = Grafo()

        lista_economia = [
        Asignatura("MAT101", "Matemática Básica", 4, 1),
        Asignatura("PIU102", "Proyección e Integración Universitaria", 3, 1),
        Asignatura("COM103", "Comunicación y Lenguaje I", 3, 1),
        Asignatura("ING104", "A1 Communicative English", 3, 1),
        Asignatura("EST105", "Estadística I", 4, 1),
        Asignatura("CAL201", "Cálculo I", 4, 2),
        Asignatura("ADM202", "Principios de Administración", 4, 2),
        Asignatura("CON203", "Contabilidad I", 4, 2),
        Asignatura("EST204", "Estadística II", 4, 2),
        Asignatura("ING205", "A2 Communicative English", 3, 2),
        Asignatura("COM206", "Comunicación y Lenguaje II", 3, 2),
        Asignatura("CAL301", "Cálculo II", 4, 3),
        Asignatura("MIC302", "Microeconomía I", 4, 3),
        Asignatura("CON303", "Contabilidad II", 4, 3),
        Asignatura("MAF304", "Matemática Financiera", 4, 3),
        Asignatura("HIS305", "Historia e Identidad Nacional", 3, 3),
        Asignatura("ING306", "A2+ Communicative English", 3, 3),
        Asignatura("MIC401", "Microeconomía II", 4, 4),
        Asignatura("COS402", "Contabilidad de Costos I", 4, 4),
        Asignatura("AMB403", "Educación Ambiental", 3, 4),
        Asignatura("FIN404", "Finanzas I", 4, 4),
        Asignatura("ING405", "B1 Communicative English", 3, 4),
        Asignatura("ORA406", "Oratoria y Negociación", 3, 4),
        Asignatura("MAC501", "Macroeconomía I", 4, 5),
        Asignatura("ECO502", "Econometría I", 4, 5),
        Asignatura("FIN503", "Finanzas II", 4, 5),
        Asignatura("COS504", "Contabilidad de Costos II", 4, 5),
        Asignatura("ING505", "B1+ Communicative English", 3, 5),
        Asignatura("DER506", "Derecho Empresarial I", 3, 5),
        Asignatura("MAC601", "Macroeconomía II", 4, 6),
        Asignatura("PLO602", "Planeación Operativa", 3, 6),
        Asignatura("HPE603", "Historia del Pensamiento Económico", 3, 6),
        Asignatura("COI604", "Comercio Internacional", 4, 6),
        Asignatura("ING605", "B2 Communicative English", 3, 6),
        Asignatura("ECO606", "Econometría II", 4, 6),
        Asignatura("BEM701", "Banca y Economía Monetaria", 4, 7),
        Asignatura("DEE702", "Desarrollo Económico", 4, 7),
        Asignatura("BRM703", "Business Risk Management", 4, 7),
        Asignatura("ESE704", "Estrategia Empresarial I", 4, 7),
        Asignatura("ADE705", "Analítica de Datos Empresariales", 4, 7),
        Asignatura("HRM706", "Human Resource Management", 3, 7),
        Asignatura("GOP801", "Gestión de Operaciones", 4, 8),
        Asignatura("POE802", "Política Económica", 4, 8),
        Asignatura("ESE803", "Estrategia Empresarial II", 4, 8),
        Asignatura("DSP804", "Diseño de Sistemas de Producción", 4, 8),
        Asignatura("EMA805", "Economía del Medio Ambiente", 3, 8),
        Asignatura("GDP806", "Gestión de Proyectos", 4, 8),
        Asignatura("EMP901", "Emprendedores", 3, 9),
        Asignatura("ETI902", "Ética Empresarial", 3, 9),
        Asignatura("PRP903", "Prácticas Profesionales", 4, 9),
        Asignatura("MET904", "Metodología de la Investigación", 4, 9),
        Asignatura("FCE1001", "Formas de Culminación de Estudios", 4, 10),
        Asignatura("RSO1002", "Responsabilidad Social", 3, 10),
        Asignatura("EAF1003", "Electiva Actividades de Facultad", 3, 10),
        ]

        for m in lista_economia:
            carreras_economia[m.codigo] = m
            grafo_economia.agregar_materia(m.codigo)

        grafo_economia.agregar_relacion("ING104", "ING205")
        grafo_economia.agregar_relacion("ING205", "ING306")
        grafo_economia.agregar_relacion("ING306", "ING405")
        grafo_economia.agregar_relacion("ING405", "ING505")
        grafo_economia.agregar_relacion("ING505", "ING605")
        grafo_economia.agregar_relacion("COM103", "COM206")

        grafo_economia.agregar_relacion("MAT101", "CAL201")
        grafo_economia.agregar_relacion("CAL201", "CAL301")
        grafo_economia.agregar_relacion("EST105", "EST204")
        grafo_economia.agregar_relacion("EST204", "ECO502")
        grafo_economia.agregar_relacion("ECO502", "ECO606")
        grafo_economia.agregar_relacion("CAL201", "MIC302")
        grafo_economia.agregar_relacion("MIC302", "MIC401")
        grafo_economia.agregar_relacion("MIC401", "MAC501")
        grafo_economia.agregar_relacion("MAC501", "MAC601")
        grafo_economia.agregar_relacion("MAC601", "BEM701")
        grafo_economia.agregar_relacion("MAC601", "POE802")
        grafo_economia.agregar_relacion("CON203", "CON303")
        grafo_economia.agregar_relacion("CON303", "COS402")
        grafo_economia.agregar_relacion("COS402", "COS504")
        grafo_economia.agregar_relacion("MAF304", "FIN404")
        grafo_economia.agregar_relacion("FIN404", "FIN503")
        grafo_economia.agregar_relacion("ESE704", "ESE803")
        grafo_economia.agregar_relacion("MET904", "FCE1001")

        self.carreras["Economia Empresarial"] = {
            "materias": carreras_economia,
            "grafo": grafo_economia
        }

        carreras_negocios = {}
        grafo_negocios = Grafo()

        lista_negocios = [
        Asignatura("ING101", "A1 Communicative English", 3, 1),
        Asignatura("COM102", "Comunicación y Lenguaje I", 3, 1),
        Asignatura("FNI103", "Fundamentos de Negocios Internacionales", 4, 1),
        Asignatura("MAT104", "Matemática Básica", 4, 1),
        Asignatura("ADM105", "Principios de Administración", 4, 1),
        Asignatura("PIU106", "Proyección e Integración Universitaria", 3, 1),
        Asignatura("IDN107", "Identidad Nacional y Orgullo Patrio", 3, 1),
        Asignatura("ING201", "A2 Communicative English", 3, 2),
        Asignatura("COM202", "Comunicación y Lenguaje II", 3, 2),
        Asignatura("CON203", "Contabilidad I", 4, 2),
        Asignatura("MKT204", "Fundamentos de Marketing", 4, 2),
        Asignatura("ECO205", "Principios de Economía", 4, 2),
        Asignatura("TGI206", "Tecnologías de Gestión de la Información", 3, 2),
        Asignatura("ING301", "A2+ Communicative English", 3, 3),
        Asignatura("DER302", "Derecho Empresarial I", 3, 3),
        Asignatura("EST303", "Estadística I", 4, 3),
        Asignatura("FIN304", "Finanzas I", 4, 3),
        Asignatura("HIS305", "Historia e Identidad Nacional", 3, 3),
        Asignatura("OMC306", "OMC y Organismos Internacionales", 4, 3),
        Asignatura("ING401", "B1 Communicative English", 3, 4),
        Asignatura("AMB402", "Educación Ambiental", 3, 4),
        Asignatura("MKT403", "Estrategias de Marketing", 4, 4),
        Asignatura("GLN404", "Globalización de los Negocios", 4, 4),
        Asignatura("INC405", "Inteligencia Comercial", 4, 4),
        Asignatura("MDN406", "Modelos de Negocios", 4, 4),
        Asignatura("ING501", "B1+ Communicative English", 3, 5),
        Asignatura("CDV502", "Cadenas de Valor", 4, 5),
        Asignatura("DDP503", "Desarrollo de Productos", 4, 5),
        Asignatura("EDI504", "Estrategias de Internacionalización", 4, 5),
        Asignatura("TDN505", "Transformación Digital en Negocios Internacionales", 4, 5),
        Asignatura("RSO506", "Responsabilidad Social", 3, 5),
        Asignatura("ING601", "B2 Communicative English", 3, 6),
        Asignatura("GDP602", "Gestión de Proyectos", 4, 6),
        Asignatura("GVI603", "Gestión de Ventas Internacionales", 4, 6),
        Asignatura("MET604", "Metodología de la Investigación", 4, 6),
        Asignatura("POC605", "Política Comercial", 4, 6),
        Asignatura("SEN606", "Seminario: Entorno Socioeconómico de los Negocios", 3, 6),
        Asignatura("EMP701", "Emprendedores", 3, 7),
        Asignatura("GAN702", "Gestión Ambiental de los Negocios Internacionales", 3, 7),
        Asignatura("INC703", "Integración Comercial", 4, 7),
        Asignatura("LEA704", "Legislación Aduanera", 4, 7),
        Asignatura("LOI705", "Logística Internacional", 4, 7),
        Asignatura("PRI706", "Propiedad Intelectual", 3, 7),
        Asignatura("ELE801", "Electiva I", 3, 8),
        Asignatura("ESE802", "Estrategia Empresarial I", 4, 8),
        Asignatura("FFM803", "Fuentes de Financiamiento y Medios de Pago", 4, 8),
        Asignatura("GEA804", "Gestión Aduanera", 4, 8),
        Asignatura("GCS805", "Gestión de la Cadena de Suministro", 4, 8),
        Asignatura("MKI806", "Marketing Internacional", 4, 8),
        Asignatura("ELE901", "Electiva II", 3, 9),
        Asignatura("ESE902", "Estrategia Empresarial II", 4, 9),
        Asignatura("GDE903", "Gestión de las Exportaciones", 4, 9),
        Asignatura("GDI904", "Gestión de las Importaciones", 4, 9),
        Asignatura("HRM905", "Human Resources Management", 3, 9),
        Asignatura("ECE1001", "Electiva de Culminación de Estudio", 4, 10),
        Asignatura("PRP1002", "Prácticas Profesionales", 4, 10),
        Asignatura("EAF1003", "Electiva de Actividades de Facultad", 3, 10),
        ]

        for m in lista_negocios:
            carreras_negocios[m.codigo] = m
            grafo_negocios.agregar_materia(m.codigo)
        
        grafo_negocios.agregar_relacion("ING101", "ING201")
        grafo_negocios.agregar_relacion("ING201", "ING301")
        grafo_negocios.agregar_relacion("ING301", "ING401")
        grafo_negocios.agregar_relacion("ING401", "ING501")
        grafo_negocios.agregar_relacion("ING501", "ING601")
        grafo_negocios.agregar_relacion("COM102", "COM202")

        grafo_negocios.agregar_relacion("FNI103", "OMC306")
        grafo_negocios.agregar_relacion("OMC306", "GLN404")
        grafo_negocios.agregar_relacion("GLN404", "EDI504")
        grafo_negocios.agregar_relacion("EDI504", "POC605")
        grafo_negocios.agregar_relacion("POC605", "INC703")
        grafo_negocios.agregar_relacion("LEA704", "GEA804")
        grafo_negocios.agregar_relacion("GEA804", "GDE903")
        grafo_negocios.agregar_relacion("GEA804", "GDI904")
        grafo_negocios.agregar_relacion("LOI705", "GCS805")
        grafo_negocios.agregar_relacion("MKT204", "MKT403")
        grafo_negocios.agregar_relacion("MKT403", "MKI806")
        grafo_negocios.agregar_relacion("CON203", "FIN304")
        grafo_negocios.agregar_relacion("FIN304", "FFM803")
        grafo_negocios.agregar_relacion("ESE802", "ESE902")
        grafo_negocios.agregar_relacion("MET604", "ECE1001")

        self.carreras["Negocios Internacionales"] = {
            "materias": carreras_negocios,
            "grafo": grafo_negocios
            }

    
        self.facultades = {

            "Facultad de Ciencias Médicas": [
                "Medicina General",
                "Psicologia",
                "Nutricion"
            ],

            "Facultad de Odontología": [
                "Odontologia"
            ],

            "Facultad de Marketing, Diseño y Ciencias de la Comunicación": [
                "Marketing y Publicidad",
                "Diseño y Comunicacion Visual",
                "Comunicacion y Relaciones Publicas"
            ],

            "Facultad de Ciencias Administrativas y Económicas": [
                "Administracion de Empresas",
                "Contabilidad y Finanzas",
                "Economia Empresarial",
                "Negocios Internacionales"
            ],

            "Facultad de Ingeniería y Arquitectura": [
                "Arquitectura",
                "Ingenieria Civil",
                "Ingenieria Industrial",
                "Ingenieria en Sistemas"
            ],

            "Facultad de Ciencias Jurídicas, Humanidades y Relaciones Internacionales": [
                "Derecho",
                "Diplomacia y Relaciones Internacionales"
            ]

        }

     
        self.seleccionar_carrera("Ingenieria en Sistemas")

    def seleccionar_carrera(self, nombre_carrera):
        buscada = nombre_carrera.strip().upper()

        for clave in self.carreras:
            if clave.strip().upper() == buscada:
                self.carrera_actual = clave
                self.materias = self.carreras[clave]["materias"]
                self.grafo = self.carreras[clave]["grafo"]
                self.aprobadas = []
                return True

        return False
    def recomendar_carga(self, promedio):

        if promedio < 0 or promedio > 100:
            return [], 0

        if promedio >= 80:
            max_creditos = 18
        else:
            max_creditos = 14

        disponibles = []

        for codigo in self.materias:

            if codigo not in self.aprobadas:

                ok, _ = self.grafo.puede_matricular(
                    codigo, self.aprobadas
                )

                if ok:
                    materia = self.materias[codigo]
                    importancia = self.grafo.contar_cadena(codigo)

                    disponibles.append((importancia, materia))

        n = len(disponibles)

        for i in range(n):
            for j in range(0, n - i - 1):
                imp_actual, mat_actual = disponibles[j]
                imp_sig, mat_sig = disponibles[j + 1]

                if (imp_actual < imp_sig) or (imp_actual == imp_sig and mat_actual.semestre > mat_sig.semestre):
                    disponibles[j], disponibles[j + 1] = disponibles[j + 1], disponibles[j]
        recomendadas = []
        creditos_totales = 0

        for importancia, materia in disponibles:

            if creditos_totales + materia.creditos <= max_creditos:
                recomendadas.append(materia)
                creditos_totales += materia.creditos

        return recomendadas, max_creditos
