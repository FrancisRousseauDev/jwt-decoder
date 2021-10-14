<h1>JWTdecode</h1>

<p>Simple python script to decode a JWT without the hassle of surfing to sites to decode it.</p>
 

<h2>Params</h2>

Variable 1: JWTtoken <br>
Variable 2: any letter like 'c' will copy to clipboard the decoded one

<h2>Usage </h2>

python main.py JWTtokenXXX copy

python main.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c copy

<h2>Docker</h2>

Application is also available in docker format, all dependencies are installed automatically. <br>

Commands <br>
.------------------------. <br>
docker build -t jwtdecode . <br>
docker run jwtdecode eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
