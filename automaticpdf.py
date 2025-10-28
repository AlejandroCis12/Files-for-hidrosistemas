import os #Operaciones del sistema de archivos y directorios
import subprocess #Ejecución de comandos del sistema (instalación de paquetes)
import sys #Acceso a variables del intérprete Python

# Función principal
def main():
    print("Divisor de PDF")
    print("=" * 40)
    
    # Buscar archivos PDF
    pdf_files = [f for f in os.listdir(".") if f.lower().endswith(".pdf")]
    
    if not pdf_files:
        print("No se encontraron archivos PDF en esta carpeta")
        print("Coloca tu archivo PDF en la misma carpeta que este script")
        return
    
    print("Archivos PDF encontrados:")
    for i, pdf in enumerate(pdf_files, 1):
        print(f"   {i}. {pdf}")
    
    # Seleccionar archivo
    if len(pdf_files) == 1:
        input_pdf = pdf_files[0]
    else:
        try:
            choice = int(input("Ingresa el número del archivo a procesar: ")) - 1
            input_pdf = pdf_files[choice]
        except (ValueError, IndexError):
            print("Selección inválida")
            return
    
    print(f"Procesando: {input_pdf}")
    
    # Intentar con el método alternativo primero
 
    # Intentar instalar PyPDF2
    try:
        import pypdf2
        print("PyPDF2 ya está instalado")
    except ImportError:
        print("Instalando PyPDF2...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf2"])
            print("PyPDF2 instalado correctamente")
        except:
            print("No se pudo instalar PyPDF2 automáticamente")
            print("Ejecuta manualmente: python -m pip install pypdf2")
            return
    
    # Ahora ejecutar el script original
    from PyPDF2 import PdfReader, PdfWriter
    
    reader = PdfReader(input_pdf)
    output_dir = "Folletos por separado"
    os.makedirs(output_dir, exist_ok=True)
    
    total_pages = len(reader.pages)
    print(f"El PDF tiene {total_pages} páginas")

    Names=["CPVC Agua caliente","Hidráulica Inglés C-40 PVC","Hidráulica Inglés C-80 PVC","Hidráulica Inglés campana PVC","Tubería Galvanizada","Toma domiciliaria","Medidores y válvulas","Alcantarillado métrico campana","Tubería de PEAD corrugado","Linea Sanitaria","Brocales y rejillas PEAR","Soportería","Tubería Eléctrica PVC Lisa y Corrugada"]
    
    for i in range(0, total_pages, 2):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        
        if i + 1 < total_pages:
            writer.add_page(reader.pages[i + 1])
        
        page_end = i + 2 if i + 1 < total_pages else i + 1
        output_filename = f"{Names[i // 2]}.pdf"
        output_path = os.path.join(output_dir, output_filename)
        
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        
        print(f"Creado: {output_filename}")
    
    print(f" Proceso completado! Se crearon {(total_pages + 1) // 2} archivos")

if __name__ == "__main__":
    main()