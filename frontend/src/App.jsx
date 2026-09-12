import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [longUrl, setLongUrl] = useState('');
  const [shortUrl, setShortUrl] = useState(null);
  const [error, setError] = useState('');
  const [copied, setCopied] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setShortUrl(null);
    setCopied(false);

    try {
      const response = await axios.post('http://localhost:8000/shortener', { url: longUrl });
      setShortUrl(response.data);
    } catch (err) {
      setError('Ошибка при сокращении ссылки');
    }
  };

  const handleCopy = () => {
    if (shortUrl?.short_url) {
      navigator.clipboard.writeText(shortUrl.short_url);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000); // Возвращаем текст кнопки через 2 сек
    }
  };

  return (
    <div className="app-container">
      <h1 className="title">✂️ Сокращатель ссылок</h1>

      <form className="form" onSubmit={handleSubmit}>
        <input
          type="url"
          className="input-field"
          placeholder="https://example.com"
          value={longUrl}
          onChange={(e) => setLongUrl(e.target.value)}
          required
        />
        <button type="submit" className="btn-primary">Сократить</button>
      </form>

      {error && <p className="error-text">{error}</p>}

      {shortUrl && (
        <div className="result-box">
          <p className="success-text">🎉 <b>Готово!</b></p>

          <div className="link-container">
            <a href={shortUrl.short_url} target="_blank" rel="noopener noreferrer" className="short-link">
              {shortUrl.short_url}
            </a>
            <button type="button" className="btn-copy" onClick={handleCopy}>
              {copied ? 'Скопировано!' : 'Копировать'}
            </button>
          </div>

          <p className="clicks-text">
            Количество переходов: <b>{shortUrl.clicks || 0}</b>
          </p>
        </div>
      )}
    </div>
  );
}

export default App;