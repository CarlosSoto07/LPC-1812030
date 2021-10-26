$Path = "C:\Users\jesus\docs"
"{0,10} {1,-24} {2,-2}" -f `
" Size", "Last Accessed", "File Name "
Foreach ($file in Get-Childitem $Path -recurse -force)
{If ($file.extension -eq ".txt")
    {
    "{0,10} {1,-24} {2,-2}" -f `
    $file.length, $file.LastAccessTime, $file.fullname
    }
}
