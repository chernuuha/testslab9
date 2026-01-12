// src/App.jsx
import { useState } from 'react';

export default function RegistrationForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    confirmPassword: '',
    agreed: false,
  });

  const [errors, setErrors] = useState({});
  const [isSubmitted, setIsSubmitted] = useState(false);

  const validate = () => {
    const newErrors = {};

    // Имя: 2–50 символов, только буквы и пробелы
    if (!formData.name.trim()) {
      newErrors.name = 'Имя обязательно для заполнения';
    } else if (formData.name.length < 2) {
      newErrors.name = 'Имя должно содержать минимум 2 символа';
    } else if (formData.name.length > 50) {
      newErrors.name = 'Имя не может быть длиннее 50 символов';
    } else if (!/^[a-zA-Zа-яА-Я\s]+$/.test(formData.name)) {
      newErrors.name = 'Имя может содержать только буквы и пробелы';
    }

    // Email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email.trim()) {
      newErrors.email = 'Email обязателен';
    } else if (!emailPattern.test(formData.email)) {
      newErrors.email = 'Некорректный формат email';
    }

    // Пароль
    if (!formData.password) {
      newErrors.password = 'Пароль обязателен';
    } else if (formData.password.length < 8) {
      newErrors.password = 'Пароль должен содержать минимум 8 символов';
    } else if (formData.password.length > 64) {
      newErrors.password =
        'Пароль не может быть длиннее 64 символов';
    }

    // Подтверждение пароля
    if (formData.password !== formData.confirmPassword) {
      newErrors.confirmPassword = 'Пароли не совпадают';
    }

    // Согласие
    if (!formData.agreed) {
      newErrors.agreed = 'Необходимо согласие с условиями';
    }

    return newErrors;
  };

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value,
    });

    // Опционально: очищать ошибку при исправлении поля
    if (errors[name]) {
      setErrors((prev) => ({ ...prev, [name]: '' }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const newErrors = validate();
    setErrors(newErrors);

    if (Object.keys(newErrors).length === 0) {
      // Форма валидна — имитируем отправку
      console.log('Форма отправлена:', formData);
      setIsSubmitted(true);
    }
  };

  if (isSubmitted) {
    return (
      <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
        <h2>✅ Регистрация прошла успешно!</h2>
        <p>Данные отправлены.</p>
        <button onClick={() => setIsSubmitted(false)}>Зарегистрироваться ещё раз</button>
      </div>
    );
  }

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif', maxWidth: '400px' }}>
      <h2>Форма регистрации</h2>
      <form onSubmit={handleSubmit}>
        {/* Имя */}
        <div style={{ marginBottom: '12px' }}>
          <label>Имя:</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            style={{ width: '100%', padding: '6px', marginTop: '4px' }}
          />
          {errors.name && <span style={{ color: 'red', fontSize: '14px' }}>{errors.name}</span>}
        </div>

        {/* Email */}
        <div style={{ marginBottom: '12px' }}>
          <label>Email:</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            style={{ width: '100%', padding: '6px', marginTop: '4px' }}
          />
          {errors.email && <span style={{ color: 'red', fontSize: '14px' }}>{errors.email}</span>}
        </div>

        {/* Пароль */}
        <div style={{ marginBottom: '12px' }}>
          <label>Пароль:</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            style={{ width: '100%', padding: '6px', marginTop: '4px' }}
          />
          {errors.password && <span style={{ color: 'red', fontSize: '14px' }}>{errors.password}</span>}
        </div>

        {/* Подтверждение пароля */}
        <div style={{ marginBottom: '12px' }}>
          <label>Подтвердите пароль:</label>
          <input
            type="password"
            name="confirmPassword"
            value={formData.confirmPassword}
            onChange={handleChange}
            style={{ width: '100%', padding: '6px', marginTop: '4px' }}
          />
          {errors.confirmPassword && (
            <span style={{ color: 'red', fontSize: '14px' }}>{errors.confirmPassword}</span>
          )}
        </div>

        {/* Согласие */}
        <div style={{ marginBottom: '16px' }}>
          <label>
            <input
              type="checkbox"
              name="agreed"
              checked={formData.agreed}
              onChange={handleChange}
              style={{ marginRight: '8px' }}
            />
            Согласен с условиями использования
          </label>
          {errors.agreed && <span style={{ color: 'red', fontSize: '14px' }}>{errors.agreed}</span>}
        </div>

        {/* Кнопка */}
        <button
          type="submit"
          style={{
            padding: '8px 16px',
            backgroundColor: '#007bff',
            color: 'white',
            border: 'none',
            cursor: 'pointer',
          }}
        >
          Зарегистрироваться
        </button>
      </form>
    </div>
  );
}