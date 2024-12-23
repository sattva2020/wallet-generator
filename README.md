# Wallet Generator

[🇬🇧 English Version](#wallet-generator-en) | [🇷🇺 Russian Version](#wallet-generator-ru)

---

<a name="wallet-generator-en"></a>
# Wallet Generator

A simple and secure cryptocurrency wallet generator for MetaMask (Ethereum) and Solana.

## 🚀 Features

- Generation of MetaMask (Ethereum) and Solana wallets
- BIP44 standard implementation for wallet creation
- All data saved to Excel, CSV, or JSON file
- Bulk creation support
- Separate mnemonic phrase generation for each wallet type
- Password protection for wallets
- **Customizable password generation**: Support for fixed or random passwords, configurable length via `settings.yaml`
- **Export formats**: Default support for `xlsx`, with options for `csv` and `json`

## 📋 Requirements
```bash
Python 3.8+
```

## ⚙️ Installation

1. Clone the repository
```bash
git clone https://github.com/username/wallet-generator.git
cd wallet-generator
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure settings.yaml
```yaml
PASSWORD_PHANTOM: "phantom_password"
PASSWORD_METAMASK: "metamask_password"
PASSWORD_WALLET: "common_wallet_password"
DISPLAY_PASSWORD: true  # Set to true to display the wallet password in the output
```

### Parameters Description

- `PASSWORD_PHANTOM`: The password for the Phantom wallet.
- `PASSWORD_METAMASK`: The password for the MetaMask wallet.
- `PASSWORD_WALLET`: The common password for the wallets.
- `DISPLAY_PASSWORD`: Set to true to display the wallet password in the output.

## 🔧 Usage

### Windows

1. Create virtual environment:
```bash
python -m venv venv
```

2. Create launch file `start_wallet_gen.bat`:
```bat
@echo off
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py
pause
```

3. Run the created file by double-clicking or via command line:
```bash
start_wallet_gen.bat
```

### MacOS/Linux
1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies and run the script:
```bash
pip install -r requirements.txt
python3 main.py
```

### Batch Script (Windows)

1. Run the setup script:
```batch
.\setup.bat
```

### PowerShell (Windows)

1. Run the setup script:
```powershell
.\setup.ps1
```

## 📁 Project Structure

```
wallet-generator/
├── main.py              # Main script
├── generate_wallet.py   # Wallet generator
├── requirements.txt     # Dependencies
├── settings.yaml       # Settings
└── README.md           # Documentation
```

## 📝 Output Format

Excel file contains the following columns:
- Mnemonic
- Solana Address
- Solana Private Key
- MetaMask Address
- MetaMask Private Key
- Wallet Password (format: 12****78)

## 🔒 Security

- All private keys are generated locally
- Mnemonic phrases are never transmitted
- Data is saved only to local Excel file
- Cryptographically secure key generation is used

## ⚠️ Important Notes

1. Store the wallet file in a secure location
2. Never share private keys with third parties
3. Keep backup copies of mnemonic phrases

## 🤝 Contributing

To contribute to the project:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License

## 👥 Support

- Create an Issue in the repository
- Contact the developers

---

<a name="wallet-generator-ru"></a>
# Генератор Криптокошельков [🇷🇺]

Простой и безопасный генератор криптовалютных кошельков для MetaMask (Ethereum) и Solana.

## 🚀 Возможности

- Генерация кошельков MetaMask (Ethereum) и Solana
- Реализация стандарта BIP44 для создания кошельков
- Сохранение всех данных в Excel файл
- Поддержка массового создания
- Генерация отдельных мнемонических фраз для каждого типа кошелька
- Защита кошельков паролем

## 📋 Требования
```bash
Python 3.8+
```

## ⚙️ Установка

1. Клонируйте репозиторий
```bash
git clone https://github.com/username/wallet-generator.git
cd wallet-generator
```

2. Установите зависимости
```bash
pip install -р requirements.txt
```

3. Настройте settings.yaml
```yaml
PASSWORD_PHANTOM: "phantom_password"
PASSWORD_METAMASK: "metamask_password"
PASSWORD_WALLET: "common_wallet_password"
DISPLAY_PASSWORD: true  # Установите значение true, чтобы отображать пароль кошелька в выводе
```

### Описание параметров

- `PASSWORD_PHANTOM`: Пароль для кошелька Phantom.
- `PASSWORD_METAMASK`: Пароль для кошелька MetaMask.
- `PASSWORD_WALLET`: Общий пароль для кошельков.
- `DISPLAY_PASSWORD`: Установите значение true, чтобы отображать пароль кошелька в выводе.

## 🔧 Использование

### Windows

1. Создайте виртуальное окружение:
```bash
python -m venv venv
```

2. Создайте файл запуска `start_wallet_gen.bat`:
```bat
@echo off
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py
pause
```

3. Запустите созданный файл двойным щелчком или через командную строку:
```bash
start_wallet_gen.bat
```

### MacOS/Linux
1. Создайте и активируйте виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Установите зависимости и запустите скрипт:
```bash
pip install -р requirements.txt
python3 main.py
```

### Batch Script (Windows)

1. Запустите скрипт настройки:
```batch
.\setup.bat
```

### PowerShell (Windows)

1. Запустите скрипт настройки:
```powershell
.\setup.ps1
```

## 📁 Структура проекта

```
wallet-generator/
├── main.py              # Основной скрипт
├── generate_wallet.py   # Генератор кошельков
├── requirements.txt     # Зависимости
├── settings.yaml       # Настройки
└── README.md           # Документация
```

## 📝 Формат вывода

Файл Excel содержит следующие столбцы:
- Мнемоническая фраза
- Адрес Solana
- Приватный ключ Solana
- Адрес MetaMask
- Приватный ключ MetaMask
- Пароль кошелька (формат: 12****78)

## 🔒 Безопасность

- Все приватные ключи генерируются локально
- Мнемонические фразы никогда не передаются
- Данные сохраняются только в локальный файл Excel
- Используется криптографически безопасная генерация ключей

## ⚠️ Важные замечания

1. Храните файл кошелька в безопасном месте
2. Никогда не делитесь приватными ключами с третьими лицами
3. Держите резервные копии мнемонических фраз

## 🤝 Вклад

Чтобы внести вклад в проект:
1. Форкните репозиторий
2. Создайте ветку с новой функцией
3. Внесите свои изменения
4. Отправьте запрос на слияние

## 📄 Лицензия

Лицензия MIT

## 👥 Поддержка

- Создайте Issue в репозитории
- Свяжитесь с разработчиками
