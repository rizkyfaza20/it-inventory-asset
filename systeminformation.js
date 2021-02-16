const info = require('systeminformation');

    info.cpu().then(data => console.log(data.manufacturer));
    info.cpu().then(data => console.log(data.brand));
