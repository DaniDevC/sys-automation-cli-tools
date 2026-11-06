import os
import shutil
import sys

# Mapeo de extensiones
EXTENSIONS_MAP = {
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.csv'],
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    'Archivos_Comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Ejecutables_Instaladores': ['.exe', '.dmg', '.pkg', '.deb'],
    'Scripts_Codigo': ['.py', '.js', '.html', '.css', '.json']
}

def organize_directory(target_dir):
    if not os.path.exists(target_dir):
        print(f"[X] La ruta especificada no existe: {target_dir}")
        return

    print(f"[*] Organizandotarget directory: {target_dir}")
    moved_files = 0

    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)

        # Saltar carpetas
        if os.path.isdir(item_path):
            continue

        filename, file_extension = os.path.splitext(item)
        file_extension = file_extension.lower()

        moved = False
        for category, extensions in EXTENSIONS_MAP.items():
            if file_extension in extensions:
                category_folder = os.path.join(target_dir, category)
                os.makedirs(category_folder, exist_ok=True)
                
                shutil.move(item_path, os.path.join(category_folder, item))
                print(f"[✔] Movido: {item} -> {category}/")
                moved_files += 1
                moved = True
                break

        # Archivos con extensiones no catalogadas
        if not moved and file_extension:
            other_folder = os.path.join(target_dir, 'Otros')
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(item_path, os.path.join(other_folder, item))
            print(f"[✔] Movido: {item} -> Otros/")
            moved_files += 1

    print(f"\n[🎉] Proceso completado. Total de archivos organizados: {moved_files}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    organize_directory(target)