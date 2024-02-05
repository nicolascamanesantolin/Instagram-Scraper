# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import wget
import warnings

#Cargar instagram
def load_instagram():
    driver.get("https://www.instagram.com/")

#Permitir sólo las cookies necesarias

def allow_cookies():
    time.sleep(4)
    driver.find_element(by=By.XPATH, value = "//button[contains(text(), 'Permitir solo cookies necesarias')]").click()

#Registrarse
def login(u, p):
    time.sleep(5)
    username = driver.find_element(by = By.XPATH,
               value = '//*[@id="loginForm"]/div/div[1]/div/label/input')
    password = driver.find_element(by = By.XPATH,
               value = '//*[@id="loginForm"]/div/div[2]/div/label/input')
    username.clear()
    password.clear()
    username.send_keys(u)
    password.send_keys(p)
    login = driver.find_element(by = By.XPATH,
            value = '//*[@id="loginForm"]/div/div[3]/button').click()

#No guardar registro
def not_save_login_info():
    time.sleep(6)
    driver.find_element(by = By.XPATH, value = '//*[@id="react-root"]/section/main/div/div/div/div/button').click()

#No habilitar notificaciones
def no_notif():
    time.sleep(4)
    driver.find_element(by = By.CSS_SELECTOR,
    value = 'body > div.RnEpo.Yx5HN > div > div > div\
             > div.mt3GC > button.aOOlW.HoLwm').click()
#Buscar usuario
def search_user(user_name):
    time.sleep(5)
    searchbox = driver.find_element(by = By.XPATH,
                value = '//*[@id="react-root"]/section/nav/\
                div[2]/div/div/div[2]/input')
    searchbox.clear()
    searchbox.send_keys(user_name)
    time.sleep(2)
    user = get_username()
    if user == user_name:
        searchbox.send_keys(Keys.ENTER)
        time.sleep(2)
        searchbox.send_keys(Keys.ENTER)
        return('Hemos encontrado el usuario con éxito')
    else:
        return('No se ha encontrado ese usuario')

def get_username():
    time.sleep(1)
    try:
        c_username = driver.find_element(by=By.XPATH, value='/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div/div/div/div[1]').text
    except:
        c_username = 'Unknown'
    return str(c_username)

def get_posts():
    time.sleep(3)
    try:
        n_posts = driver.find_element(by = By.XPATH, value='/html/body/div[1]/section/main/div/header/section/ul/li[1]/div/span').text
    except:
        n_posts = '0'
    return n_posts

def get_followers():
    try:
        n_followers = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div/span').text
    except:
        n_followers = '0'
    return n_followers

def get_following():
    try:
        n_following = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div/span').text
    except:
        n_following = '0'
    return n_following

def get_name():
    try:
        full_name = driver.find_element(by = By.XPATH, value= '/html/body/div[1]/section/main/div/header/section/div[2]/span').text
    except:
        full_name = 'Unknown'
    return full_name

def get_role():
    try:
        role = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/section/main/div/header/section/div[2]/div[1]/div').text
    except:
        role = 'Unknown'
    return role

def get_descrip():
    try:
        descrip = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/section/main/div/header/section/div[2]/div[2]').text
    except:
        try:
            descrip = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/section/main/div/header/section/div[2]/div').text
        except:
            descrip = 'Unknown'
    return descrip

def get_link():
    try:
        address= driver.find_element(by = By.XPATH, value = '/html/body/div[1]/section/main/div/header/section/div[2]/a/div').text
    except:
        address = 'Unknown'
    return address

#Recorrer el perfil y ir guardando los url de los posts y los url de la imagen de cada post
def scroll_posts_images():
    time.sleep(6)
    posts = []
    scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    match=False
    while(match==False):
        #Collecting posts url
        links_posts = driver.find_elements(by = By.TAG_NAME, value = 'a')
        for link in links_posts:
            post = link.get_attribute('href')
            if (post not in posts) and ('/p/' in post):
                  posts.append(post)
        last_count = scrolldown
        time.sleep(7)
        scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
        time.sleep(2)
        if last_count==scrolldown:
            match=True
    return posts

def get_images(posts, condicion):
    images = []
    likes = []
    coments = []
    for a in posts:
        driver.get(a)
        time.sleep(5)
        try:
            like = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[2]/div/div/div/a/div/span').text
        except:
            try:
                like = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[2]/div/span/div/span').text
            except:
                like = 'Unknown'
        likes.append(like)
        try:
            coment = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/div/li/div/div/div[2]/div[1]/span').text
        except:
            coment = 'Unknown'
        coments.append(coment)
        if condicion == 'si':
            try:
                    vid = driver.find_element(by=By.TAG_NAME, value='video')
                    vid=vid.get_attribute('poster')
                    images.append(vid)

            except:
                try:
                    img = driver.find_element(by=By.TAG_NAME, value='img')
                    time.sleep(4)
                    img = img.get_attribute('src')
                    images.append(img)
                except:
                    images.append('Not found')
    return (images, likes, coments)

#Creamos una carpera principal (si no existe)
def create_general_folder(user_name):
    #Crear carpera si no existe
    if(os.path.isdir(user_name) == False):
            os.mkdir(user_name)
    return (os.path.dirname(os.path.abspath(__file__))+user_name)

def save_profile_info(n_posts, n_followers, n_following, full_name, role, descrip, link_gived):
    f= open(str(user_name)+'/'+'profile_info'+'.txt','w')
    f.write('Number of posts:    '+'\t'+str(n_posts)+'\n')
    f.write('Number of followers:'+'\t'+str(n_followers)+'\n')
    f.write('Number of following:'+'\t'+str(n_following)+'\n')
    f.write('Full name:         '+'\t'+str(full_name)+'\n')
    f.write('Role:               '+'\t'+str(role)+'\n')
    f.write('Description :       '+'\t'+str(descrip)+'\n')
    f.write('Link in the bio:    '+'\t'+str(link_gived)+'\n')
    f.close()

#Dejar url de cada post en un txt
def posts_txt(user_name, url_posts, likes_posts, coments_posts):
    f = open (str(user_name)+'/'+'url_of_posts'+'.txt','w')
    for i in range(len(url_posts)):
        f.write('Post '+str(i)+':'+'\t'+url_posts[i]+'\n'+ 'Likes/Reproductions:'+'\t'+str(likes_posts[i])+'\n'+ 'Description:'+'\n'+coments_posts[i]+'\n')
        f.write('\n')
    f.close()

#Crear carpera si no existe para los posts descargados
def create_posts_folder(user_name):
    director_for_posts = user_name+'/downloaded_posts'
    if(os.path.isdir(director_for_posts) == False):
            # Create folder
            os.mkdir(director_for_posts)
    return (os.path.dirname(os.path.abspath(__file__)) + director_for_posts, director_for_posts)

#Descargar posts en el directorio
def download_images(images, posts_folder):
    counter = 0
    for img in images:
        if img != 'Not found':
            save_as = os.path.join(posts_folder, 'posts_image_'+str(counter)+".jpg")
            wget.download(img, save_as)
            counter += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # PRIMERA FASE
    warnings.filterwarnings('ignore')
    PATH = "/home/nicolas/PycharmProjects/Instagram-Scraper2/chromedriver"
    usuario = 'proyecto.seguridad.nicolas'
    contra = 'Elcamionquederrapa'
    print('BIENVENIDO AL EXTRACTOR DE INSTAGRAM')
    print('Mediante este programa vas a poder obtener información general de un perfil de ususario y además información de cada post del usuario')
    driver = webdriver.Chrome(PATH)
    load_instagram()
    allow_cookies()
    login(usuario, contra)
    not_save_login_info()
    no_notif()
    # SEGUNDA FASE
    user_name = input('Ahora introduce el usuario al que vamos a realizar la extracción: ')
    encontrado = search_user(user_name)
    while encontrado == 'No se ha encontrado ese usuario':
        user_name = input('No se ha encontrado ese usuario, vuelve a introducir el usuario que deseas scrapear: ')
        encontrado = search_user(str(user_name))
    print("Hemos encontrado el usuario, vamos a proceder con la extracción")
    # TERCERA FASE
    number_posts = get_posts()
    number_followers = get_followers()
    number_following = get_following()
    profile_name = get_name()
    profile_role = get_role()
    profile_descrip = get_descrip()
    profile_link = get_link()
    ruta_general = create_general_folder(user_name)
    save_profile_info(number_posts, number_followers, number_following, profile_name, profile_role, profile_descrip, profile_link)
    # CUARTA FASE
    print("Estamos recorriendo el perfil mientras recogemos información")
    posts = scroll_posts_images()
    print("Ademaś, ¿también deseas descargear las imágenes?(si/no):", end=" ")
    cond_imagenes = input()
    while cond_imagenes != 'si' and cond_imagenes != 'no':
        cond_imagenes = input("Parece que no has introducido bien la resuesta, ¿deseas descargear las imágenes?(si/no): ")
    if cond_imagenes == 'si': print("A conticuación, descargaremos las imagenes")
    else: print('No descargaremos las imagenes')
    (images, likes, coments) = get_images(posts, cond_imagenes)
    posts_txt(user_name, posts, likes, coments)
    print('La ruta absoluta del directorio que hemos creado para guardar la informacion es: ',ruta_general)
    if cond_imagenes == 'si':
        (full_path, folder_path) = create_posts_folder(user_name)
        print('La ruta absoluta del directorio que hemos creado para guardar las imagenes es: ', full_path)
        download_images(images, folder_path)
    print('\nLA EXTRACCIÓN HA FINALIZADO CON ÉXITO, HASTA LA PRÓXIMA')


