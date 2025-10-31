from PIL import Image
import os
from pathlib import Path

def resize_profile_image(input_path, output_size=(500, 500)):
    """Redimensionar imagen de perfil a tamaño cuadrado"""
    try:
        with Image.open(input_path) as img:
            # Convertir a RGB si es necesario
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Redimensionar manteniendo relación de aspecto
            img.thumbnail(output_size, Image.Resampling.LANCZOS)
            
            # Crear imagen cuadrada con fondo blanco
            squared_img = Image.new('RGB', output_size, (255, 255, 255))
            
            # Pegar la imagen redimensionada en el centro
            offset = ((output_size[0] - img.size[0]) // 2, 
                     (output_size[1] - img.size[1]) // 2)
            squared_img.paste(img, offset)
            
            # Guardar
            output_path = Path(__file__).parent / "static" / "images" / "profile" / "Foto de perfil.png"
            squared_img.save(output_path, "JPEG", quality=85)
            
            print(f"Imagen redimensionada y guardada en: {output_path}")
            print(f"Tamaño final: {output_size[0]}x{output_size[1]} píxeles")
            
            return True
            
    except Exception as e:
        print(f"Error procesando imagen: {e}")
        return False

if __name__ == "__main__":
    # Reemplaza con la ruta de TU imagen
    tu_imagen = input("Introduce la ruta completa de tu imagen: ").strip().strip('"')
    
    if os.path.exists(tu_imagen):
        resize_profile_image(tu_imagen)
    else:
        print("La ruta especificada no existe")