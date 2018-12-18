@echo off

SET PORT=3571
SET COMMAND=%1
SET TYPE=%2
SET NAME=%3
SET URL=%4
SET GIT_REPOSITORY="https://github.com/zoltancsontos/pystack-framework.git" %NAME%

IF NOT DEFINED COMMAND (SET COMMAND=help)

IF "%COMMAND%"=="create" (
    IF "%TYPE%"=="app" (
        git clone %GIT_REPOSITORY%
        cd %NAME%
        rm -rf .git
        goto exit
    ) ELSE (
        python pystack.py %*
    )
)
IF "%COMMAND%"=="run" (
   python pystack.py %*
)
IF "%COMMAND%"=="help" (
    echo.
    echo ==========================================================================================
    echo                              PyStack Framework v1.0
    echo ==========================================================================================
    echo.
    echo List of CLI options:
    echo.
    echo pystack-cli create app appName - creates a new pystack application with the specified name
    echo pystack-cli run --port=port - runs the application on the specified port
    echo pystack-cli create page PageName page-url - creates a page
    echo pystack-cli create resource ResourceName resource-url - creates a standard rest api
    echo.
)

:exit