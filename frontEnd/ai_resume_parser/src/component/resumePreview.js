import React from "react"

const FilePreview = (file) =>{

if (!file){
    return "No file"
}

fileUrl = URL.createObjectURL(file);

if (file.type==="application.pdf")
    return (
        <div>
            <p>
                <h1>Resume Preview</h1>
            </p>
            <iframe src="fileUrl" height="600 px" width="600 px" title="Resume Preview">
                
            </iframe>
        </div>
    );
 
}
export default FilePreview;