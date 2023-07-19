from flask import Flask, render_template, request
from library import AES,pad,rsa,serialization,hashes,padding,Blowfish,get_random_bytes, ec,Cipher, algorithms, modes,default_backend

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/home', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        ciphertext = ''
        
        if 'aes' in request.form:   # aes encrytpion implementation

            key = b'sixteen byte key' # the key and 'initialization vector' used for AES encryption
            iv = b'InitializationVe'

            cipher = AES.new(key, AES.MODE_CBC, iv) #create the AES cipher object

            plaintext = pad(text.encode(), AES.block_size) #pading the plaintext to match AES block size
            
            ciphertext = cipher.encrypt(plaintext) #encryption of the plain text

        elif 'rsa' in request.form: # RSA implementation
            
            private_key = rsa.generate_private_key( # generating the RSA key pairs used for encryption
                public_exponent=65537,
                key_size=2048
        )
            public_key = private_key.public_key()

            plaintext = text.encode() #converting the text to bytes to properly process the data

            ciphertext = public_key.encrypt( #encryption of plain text using RSA public key
                plaintext,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        
        elif 'blowfish' in request.form: # BLOWFISH encryption

            key = get_random_bytes(16) # generate a random 16-byte key for encryption

            cipher = Blowfish.new(key, Blowfish.MODE_CBC) #creating a Blowfish cipher object with the key

            plaintext = pad(text.encode(), Blowfish.block_size) #padding the plaintext to match the blowfish block size

            ciphertext = cipher.encrypt(plaintext) #plain text encryption

        return render_template('index.html', ciphertext=ciphertext)
    return render_template('index.html')

@app.route('/about',methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/blog',methods=['GET', 'POST'])
def blog():
    return render_template('blog.html')

if __name__ == '__main__':
   app.run(debug=True)