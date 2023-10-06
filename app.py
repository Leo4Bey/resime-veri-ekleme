from PIL import Image, ImageDraw, ImageFont

# Resim dosyasını yükleyin
image_path = 'deneme.png'
image = Image.open(image_path)

# Resmin üzerine yazı eklemek için bir draw nesnesi oluşturun
draw = ImageDraw.Draw(image)

# Kullanmak istediğiniz yazı ve fontu belirleyin
text = "Leo4Code"
font = ImageFont.truetype("arial.ttf", 96) 

# Yazıyı resmin üzerine ekleyin (koordinatları ve renk seçeneklerini ayarlayabilirsiniz)
position = (300, 150)  # Yazının konumu (x, y)
text_color = (255, 25, 25)  # Beyaz renk (RGB)
draw.text(position, text, fill=text_color, font=font)

# Yeni resmi kaydedin veya görüntüleyin
output_path = 'output.png'
image.convert('RGB').save(output_path)
image.show()