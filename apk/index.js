/**
 * @format
 */


import {AppRegistry} from 'react-native';
import App from './src/App';  // ← Updated path
import {name as appName} from './app.json';

AppRegistry.registerComponent(appName, () => App);
