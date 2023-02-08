module.exports = {
  env: {
    es2021: true,
    node: true
  },
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module'
  },
  rules: {
    // switch case 會與 prettier 衝突
    // ref: https://stackoverflow.com/questions/56280222/airbnb-eslint-prettier-conflict-over-switch-and-case-indentation
    indent: [
      'error',
      2,
      { SwitchCase: 1, ignoredNodes: ['PropertyDefinition'] }
    ],
    quotes: ['error', 'single', 'avoid-escape'],
    semi: ['error', 'always']
  }
};
  