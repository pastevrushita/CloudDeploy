from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return """
    <!DOCTYPE html> 
    <html lang="en"> 
    <head> 
     <meta charset="UTF-8"> 
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>CloudPulse</title> <style> 
      * { box-sizing: border-box; 
          margin: 0; 
          padding: 0; 
        } 
        body { font-family: Arial, sans-serif;
               background:white; 
               color: #0f172a; 
               min-height: 100vh; 
        } 
         header { background: #1e293b; 
                  padding: 20px 40px; 
                  display: flex; 
                  justify-content: space-between; 
                  align-items: center; 
                  border-bottom: 1px solid #334155; 
        } 
        .logo { font-size: 26px; 
                font-weight: bold;
                color:white; 
        } 
        .aws-status { color: #22c55e; 
                      font-weight: bold; 
        }  
        .container { max-width: 900px; 
                     margin: 50px auto; 
                     padding: 20px; 
        } 
        .title { text-align: center;
                 margin-bottom: 35px;
        } 
        .title h1 { font-size: 36px; 
                    margin-bottom: 10px;
        } 
        .title p { color: #94a3b8; } 
         
        .card { background: #1e293b; 
                border: 1px solid #334155; 
                border-radius: 15px; 
                padding: 30px; 
                margin-bottom: 25px; 
        } 
        .card-header { display: flex; 
                       justify-content: space-between; 
                       align-items: center; 
                       margin-bottom: 25px; 
        } 
        .card-header h2 { font-size: 22px; 
                          color:white; } 
        .running { color: #22c55e; 
                   font-weight: bold; 
        }  
        .details { display: grid; 
                   grid-template-columns: repeat(3, 1fr); 
                   gap: 20px; 
        } 
        .detail-box { background: #0f172a; 
                      padding: 20px; 
                      border-radius: 10px; 
        } 
        .label { color: #94a3b8; 
                 font-size: 14px; 
                 margin-bottom: 8px; 
        } 
        .value { font-size: 17px; 
                 font-weight: bold;
                 color:white; 
        }  
        
        .services { display: grid; 
                    grid-template-columns: repeat(3, 1fr); gap: 15px; 
        } 
        .service { background: #0f172a; 
                   padding: 20px; 
                   border-radius: 10px; 
                   text-align: center; 
        } 
        .service-icon { font-size: 30px; 
                        margin-bottom: 10px; 
        } 
        .service-name { font-weight: bold; 
                        margin-bottom: 8px;
                        color:white; 
        } 
        .active { color: #22c55e; 
                  font-size: 14px;
        } 
        .success { text-align: center; 
                   padding: 35px; background: #1e293b; 
                   border: 1px solid #22c55e; 
                   border-radius: 15px; 
                   margin-top: 30px; 
        } 
        .success h2 { color: #22c55e; 
                      margin-bottom: 12px; 
        } 
        .technologies { color: #94a3b8; } 
        footer { text-align: center; 
                 color: #64748b; 
                 padding: 30px; 
        } 
        @media (max-width: 700px) { 
                header { padding: 20px; } 
                .container { margin: 30px auto; } 
                .details, .services { grid-template-columns: 1fr; } 
                .title h1 { font-size: 28px; } 
        } 
        </style> 
        </head> 
        <body> 
        <!-- HEADER --> <header> <div class="logo"> CloudPulse </div> <div class="aws-status"> AWS EC2 🟢 </div> 
        </header> 
        <!-- MAIN CONTENT --> 
        <div class="container">
         
          <!-- PAGE TITLE -->
          <div class="title"> 

             <h1>Cloud Deployment Dashboard</h1>
               <p> Monitor your cloud application </p> 
          </div> 
          
          <!-- EC2 SERVER CARD -->
          <div class="card"> 
           <div class="card-header"> 
            <h2> 🖥️ EC2 SERVER </h2> 
            <span class="running"> 🟢 RUNNING </span> 
           </div> 

           <div class="details"> 
            <div class="detail-box"> 
             <div class="label"> Region </div> 
             <div class="value"> ap-south-1 </div> 
            </div> 

            <div class="detail-box"> 
             <div class="label"> Status </div> 
             <div class="value"> Online </div> 
            </div> 

            <div class="detail-box"> 
             <div class="label"> Platform </div> 
             <div class="value"> Ubuntu </div> 
            </div>
          </div> 
         </div> 

         <!-- SERVICES CARD --> 
         <div class="card"> 
          <div class="card-header"> 
           <h2>  SERVICES </h2> 
          </div> 
         <div class="services"> 
           <div class="service"> 
            <div class="service-icon"> 🐳 </div> 
            <div class="service-name"> Docker </div> 
            <div class="active"> 🟢 RUNNING </div> 
           </div> 
           <div class="service"> 
            <div class="service-icon"> 🐍 </div> 
            <div class="service-name"> Python App </div> 
            <div class="active"> 🟢 ACTIVE </div> 
           </div> 
           <div class="service"> 
            <div class="service-icon"> 🐙 </div> 
             <div class="service-name"> GitHub </div> 
             <div class="active"> 🟢 CONNECTED </div>
            </div> 
           </div> 
          </div> 
          <!-- SUCCESS SECTION --> 
          <div class="success"> 
           <h2>  Cloud Deployment Successful </h2> 
          </div> 
         </div> 
         <!-- FOOTER --> 
          <footer> Cloud Deployment Project </footer> 
        </body> 
    </html>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)