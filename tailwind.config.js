/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./pages/**/*.{html,js}",
    "./src/**/*.{js,ts,jsx,tsx}",
    "./assets/**/*.{js,html}"
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f6faf7',
          100: '#e7f2ea',
          200: '#cde3d4',
          300: '#a9c9b0',
          400: '#7ea884',
          500: '#5d8a67',
          600: '#4f7a58',
          700: '#426246',
          800: '#354f36',
          900: '#273d29'
        },
        accent: {
          50: '#fff6f1',
          100: '#ffebe0',
          200: '#ffd3bf',
          300: '#ffb185',
          400: '#ff8b51',
          500: '#f5692e',
          600: '#d04f24',
          700: '#a43e1f',
          800: '#7f301b',
          900: '#612517'
        }
      },
      boxShadow: {
        soft: '0 20px 60px rgba(15, 23, 42, 0.08)',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        display: ['Playfair Display', 'Georgia', 'serif'],
      }
    },
    screens:{
      xs: '0px',
      sm: '640px',
      md: '768px',
      lg: '1024px',
      xl: '1280px',
      '2xl': '1536px',
    },
  },
  plugins: [],
}

