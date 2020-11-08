module.exports = {
  env: {
    browser: true,
    es2021: true
  },
  extends: [
    "plugin:vue/essential",
    "standard",
    "eslint:recommended",
    "plugin:prettier/recommended"
  ],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: "module"
  },
  plugins: ["vue"],
  rules: {}
};
