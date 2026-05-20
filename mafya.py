import os
from flask import Flask, render_template_string

app = Flask(__name__)

# Berlin 1978 - Dünyaya Açılacak Tasarım Şablonu
GORUNUS_TASARIMI = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Berlin 1978 - Arayüz Testi</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { 
            background-color: #0b0c10; 
            color: #c5c6c7; 
            font-family: 'Segoe UI', sans-serif;
            padding: 10px;
        }
        .header {
            text-align: center;
            padding: 15px 0;
            border-bottom: 2px solid #1f2833;
            background: linear-gradient(180deg, #151a21 0%, #0b0c10 100%);
        }
        .header h1 { color: #66fcf1; font-size: 26px; letter-spacing: 3px; font-weight: 900; }
        .header p { color: #ff4545; font-size: 11px; letter-spacing: 1px; margin-top: 3px; }
        .profile-section {
            background-color: #151a21;
            border: 1px solid #1f2833;
            border-radius: 8px;
            padding: 12px;
            margin: 10px 0;
            display: flex;
            align-items: center;
        }
        .avatar-placeholder {
            width: 60px;
            height: 60px;
            background-color: #1f2833;
            border: 2px solid #66fcf1;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            margin-right: 15px;
        }
        .profile-info h4 { color: #fff; font-size: 16px; }
        .profile-info p { color: #858687; font-size: 12px; }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            margin-bottom: 15px;
        }
        .stat-card {
            background-color: #1f2833;
            border-radius: 6px;
            padding: 10px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }
        .stat-label { font-size: 10px; color: #a4a5a6; text-transform: uppercase; }
        .stat-value { font-size: 15px; font-weight: bold; margin-top: 4px; }
        .m-money { color: #45f3ff; }
        .m-rep { color: #ff4545; }
        .m-crew { color: #ffeb3b; }
        .section-title {
            font-size: 14px;
            color: #66fcf1;
            text-transform: uppercase;
            margin: 15px 0 8px 5px;
            letter-spacing: 1px;
            border-left: 3px solid #66fcf1;
            padding-left: 8px;
        }
        .game-card {
            background-color: #151a21;
            border: 1px solid #1f2833;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 12px;
            position: relative;
            overflow: hidden;
        }
        .game-card h3 { color: #fff; font-size: 16px; margin-bottom: 5px; }
        .game-card p { font-size: 12px; color: #858687; margin-bottom: 12px; }
        .card-badge {
            position: absolute;
            top: 15px;
            right: 15px;
            background-color: #1f2833;
            color: #66fcf1;
            padding: 2px 8px;
            font-size: 11px;
            border-radius: 10px;
            border: 1px solid #66fcf1;
        }
        .action-btn {
            background-color: #66fcf1;
            color: #0b0c10;
            border: none;
            padding: 10px 15px;
            font-size: 14px;
            font-weight: bold;
            border-radius: 4px;
            width: 100%;
            cursor: pointer;
        }
        .action-btn:active { background-color: #45f3ff; }
        .danger-btn { background-color: #ff4545; color: #fff; }
        .danger-btn:active { background-color: #ff6666; }
        .bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #151a21;
            border-top: 2px solid #1f2833;
            display: flex;
            justify-content: space-around;
            padding: 10px 0;
            z-index: 100;
        }
        .nav-item { color: #858687; text-decoration: none; font-size: 12px; text-align: center; }
        .nav-item.active { color: #66fcf1; font-weight: bold; }
        .spacer { height: 70px; }
    </style>
</head>
<body>

    <div class="header">
        <h1>BERLIN 1978</h1>
        <p>YERALTI İMPARATORLUĞU PROTOTİPİ</p>
    </div>

    <div class="profile-section">
        <div class="avatar-placeholder">🕶️</div>
        <div class="profile-info">
            <h4>Patron (Gaddar)</h4>
            <p>Rütbe: Sokak Serserisi</p>
        </div>
    </div>

    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-label">Nakit Para</div>
            <div class="stat-value m-money">5,000 DM</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Saygınlık</div>
            <div class="stat-value m-rep">120</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Tetikçiler</div>
            <div class="stat-value m-crew">3 / 10</div>
        </div>
    </div>

    <div class="section-title">Gayrimeşru İşletmeler</div>
    
    <div class="game-card">
        <div class="card-badge">Seviye 1</div>
        <h3>Kreuzberg Kaçak Deposu</h3>
        <p>Gelir: +150 DM / 5 Saniye. Mal sevkiyatını buradan yönet.</p>
        <button class="action-btn">Kapasiteyi Arttır (1,200 DM)</button>
    </div>

    <div class="game-card">
        <div class="card-badge" style="color: #858687; border-color: #333;">Kilitli</div>
        <h3 style="color: #555;">Alexanderplatz Gece Kulübü</h3>
        <p>Gelir: +500 DM / 5 Saniye. Şehrin en büyük kulübü.</p>
        <button class="action-btn" style="background-color: #333; color: #666;" disabled>Satın Al (10,000 DM)</button>
    </div>

    <div class="section-title">Sokak Operasyonları</div>

    <div class="game-card" style="border-color: #ff4545;">
        <h3>Kaçakçılık Sevkiyatı Yap</h3>
        <p>Risk: %30 | Ödül: 2,500 DM ve +20 Saygınlık</p>
        <button class="action-btn danger-btn">Operasyonu Başlat</button>
    </div>

    <div class="spacer"></div>

    <div class="bottom-nav">
        <a href="#" class="nav-item active">🏢 <br>İşletmeler</a>
        <a href="#" class="nav-item">🔫 <br>Operasyonlar</a>
        <a href="#" class="nav-item">📊 <br>Liderler</a>
    </div>

</body>
</html>
"""

@app.route('/')
def ana_sayfa():
    return render_template_string(GORUNUS_TASARIMI)

if __name__ == '__main__':
    # Railway'in port yönetimini dinamik olarak yakalıyoruz
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
