import React from "react"

const FilePreview = (file) =>{

if (!file){
    return "No file"
}

fileUrl = URL.createObjectURL(file);


}