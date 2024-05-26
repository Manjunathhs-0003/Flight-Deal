<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Flight Deal</h1>

  <h2>Overview</h2>
    <p>The Flight Deal Finder project utilizes the Sheety API, Tequila API, and Google Sheets to track and alert users about flight deals. Users can input their destination cities, and the program will check for flight deals, updating a Google Sheets spreadsheet and sending notifications when deals are found.</p>

  <h2>Features</h2>
    <ul>
        <li>User-friendly command-line interface for entering destination details.</li>
        <li>Automatic recording of flight data in a Google Sheets spreadsheet.</li>
        <li>Real-time tracking of flight prices and alert notifications.</li>
    </ul>

  <h2>How the Project Works</h2>
    <ol>
        <li><strong>User Input:</strong> Users input their destination cities through a command-line interface.</li>
        <li><strong>Tequila API:</strong> The entered city details are sent to the Tequila API to retrieve flight information.</li>
        <li><strong>Sheety API:</strong> The retrieved flight data is then sent to the Sheety API, which stores it in a Google Sheets spreadsheet.</li>
        <li><strong>Google Sheets:</strong> The flight data is updated in real-time in the Google Sheets spreadsheet, allowing users to track flight prices.</li>
        <li><strong>Notification:</strong> When a deal is found, users receive an email notification with the flight details.</li>
    </ol>

  <h2>Installation Guide</h2>
    
   <h3>Clone the Repository</h3>
    <pre><code>git clone https://github.com/Manjunathhs-0003/Flight-Deal.git</code></pre>
    
   <h3>Navigate to the Project Directory</h3>
    <pre><code>cd Flight-Deal</code></pre>
    
  <h3>Install Required Libraries</h3>
    <pre><code>pip install requests smtplib twilio</code></pre>
        <h3>Set Up API Keys and Endpoints</h3>

  <h4>Sheety API</h4>
    <ol>
        <li>Sign up or log in to Sheety <a href="https://sheety.co/">Sheety</a>.</li>
        <li>Create a new project or select an existing one.</li>
        <li>In your project settings, you will find your Sheety API key.</li>
        <li>Note the endpoints for your project (e.g., prices and users).</li>
    </ol>

  <h4>Tequila API</h4>
    <ol>
        <li>Go to the Tequila API <a href="https://tequila.kiwi.com/portal/login">Tequila API</a>.</li>
        <li>Sign up or log in.</li>
        <li>Obtain your API key from the dashboard.</li>
    </ol>
    <h4>Google Sheets API</h4>
    <ol>
        <li>Go to the Google Developers Console <a href="https://console.developers.google.com/">Google Developers Console</a>.</li>
        <li>Create a new project or select an existing one.</li>
        <li>Enable the Google Sheets API for your project.</li>
        <li>Create credentials for your project and download the JSON file containing your client secret.</li>
        <li>You will use this file to authenticate requests to the Google Sheets API.</li>
    </ol>
</body>
</html>
