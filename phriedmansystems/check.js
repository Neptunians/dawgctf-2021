const { subtle } = require('webcrypto').webcrypto;
// crypto = require('crypto');

async function checkUser(user) {
    console.log("Checking username validity...");
    const username = user;
    const hashval = await sha256(username);
    console.log("Username: " + username + "\nHashed: " + hashval);
    fetch("/secure/users/" + hashval)
        .then(response => {
            if (response.status == 200) {
                console.log(`User "${username}" exists!`);
                document.getElementById("password").disabled = false;
                document.getElementById("password").placeholder = "Enter password...";
                document.getElementById("login").disabled = false;
                document.getElementById("userValid").innerText = `User "${username}" exists! Please enter password.`;
            } else {
                console.log(`User "${username}" does not exist.`);
                document.getElementById("userValid").innerText = `User "${username}" does not exist. Cannot continue.`;
            }
        });
}

async function login(user, pwd) {
    console.log("Attempting to get secure data...");
    const username = user;
    const password = pwd;
    const input = username + "-" + password;
    const hashval = await sha256(input);
    console.log("Input: " + input + "\nHashed: " + hashval);
    fetch("/secure/data/" + hashval)
        .then(response => {
            if (response.status == 200) {
                alert(`Login with user "${username}" successful!`);
                return response.text();
            } else {
                console.warn("Login failed.");
            }
        })
        .then(data => {
            if (data == undefined) data = "<< LOGIN FAILED >>\nEnsure password is correct.";
            console.log("Data: " + data);
            document.getElementById("dataOutput").innerText = data;
            document.getElementById("userOutput").innerHTML = " of user <u>" + username + "</u>";
        });
}

// from MDN
async function sha256(message) {
    const msgUint8 = new TextEncoder().encode(message); // encode as (utf-8) Uint8Array
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgUint8); // hash the message
    // const hashBuffer = await subtle.digest('SHA-256', msgUint8); // hash the message
    const hashArray = Array.from(new Uint8Array(hashBuffer)); // convert buffer to byte array
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join(''); // convert bytes to hex string
    return hashHex;
}

param = process.argv[2];

console.log('Param: ' + param);
checkUser(param);