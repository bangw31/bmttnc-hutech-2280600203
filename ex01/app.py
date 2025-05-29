from flask import Flask, render_template, request, jsonify # Thêm jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.Playfair import PlayfairCipher
from cipher.Transposition import TranspositionCipher

app = Flask(__name__)

# ====================== CIPHER INSTANCES ======================
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayfairCipher()
transposition_cipher = TranspositionCipher()


# ====================== ROUTES ĐỂ PHỤC VỤ HTML PAGES ======================
@app.route('/')
def home():
    """Trang chủ hiển thị danh sách các thuật toán."""
    return render_template('index.html')

@app.route('/caesar')
def caesar_page():
    """Trang Caesar Cipher."""
    return render_template('caesar.html')

# Thêm routes cho các trang HTML mới
@app.route('/vigenere')
def vigenere_page():
    return render_template('vigenere.html')

@app.route('/railfence')
def railfence_page():
    return render_template('railfence.html')

@app.route('/playfair')
def playfair_page():
    return render_template('playfair.html')

@app.route('/transposition')
def transposition_page():
    return render_template('transposition.html')

# (Giả sử bạn cũng sẽ có một trang RSA HTML)
# @app.route('/rsa')
# def rsa_page():
#     return render_template('rsa.html')


# ====================== CAESAR CIPHER ENDPOINTS ======================
# Sử dụng request.form cho các endpoint này để khớp với việc gửi form từ HTML
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt_api(): # Đổi tên hàm để tránh trùng với hàm cũ trong app.py
    # Debugging: print(request.form)
    plain_text = request.form['inputText'] # Đảm bảo tên trường khớp với HTML
    key = int(request.form['key']) # Đảm bảo tên trường khớp với HTML

    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text}) # Trả về JSON


@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt_api(): # Đổi tên hàm để tránh trùng với hàm cũ trong app.py
    # Debugging: print(request.form)
    cipher_text = request.form['inputText'] # Đảm bảo tên trường khớp với HTML
    key = int(request.form['key']) # Đảm bảo tên trường khớp với HTML

    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text}) # Trả về JSON

# ====================== VIGENERE CIPHER ENDPOINTS ======================
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt_api():
    data = request.json # Hoặc request.form nếu bạn gửi từ form HTML
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt_api():
    data = request.json # Hoặc request.form
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# ====================== RAIL FENCE CIPHER ENDPOINTS ======================
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt_api():
    data = request.json # Hoặc request.form
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt_api():
    data = request.json # Hoặc request.form
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# ====================== PLAYFAIR CIPHER ENDPOINTS ======================
# Playfair thường có creatematrix riêng, nhưng ở đây tôi sẽ giữ các endpoint chính
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt_api():
    data = request.json # Hoặc request.form
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key) # Tạo matrix ngay khi mã hóa
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt_api():
    data = request.json # Hoặc request.form
    cipher_text = data['cipher_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key) # Tạo matrix ngay khi giải mã
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})

# ====================== TRANSPOSITION CIPHER ENDPOINTS ======================
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt_api():
    data = request.json # Hoặc request.form
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt_api():
    data = request.json # Hoặc request.form
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# ====================== MAIN ======================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)