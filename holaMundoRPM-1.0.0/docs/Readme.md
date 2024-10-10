#holaMundoRPM

El proyecto **\"holaMundoRPM\"** es un proyecto ejemplo de como empaquetar
un programa como holaMundoRPM.c en RPM.

## Creación del RPM:

Para crear un RPM se requieren los siguientes pasos:

1.  Instalar la herramienta rpmdevtools.

  ```bash
  \$ sudo urpmi rpmdevtools
  ```

2.  Ejecutar el comando rpmdev-setuptree, este comando crea la
    estructura para la construcción del archivo RPM.
  ```bash
  \$ rpmdev-setuptree

  Al finalizar, se abra creado la siguiente estructura:

  /home/user/rpmbuild/
  ├── BUILD
  ├── BUILDROOT
  ├── RPMS
  ├── SOURCES
  ├── SPECS
  └── SRPMS

  SOURCES: Aquí se pone el código fuente o archivos que quieras empaquetar, un archivo .tar.gz.
  SPECS: Aquí se pone el archivo .spec.
  BUILD: Lugar temporal para compilar.
  RPMS: Aquí se guardarán los archivos RPM construidos.
  SRPMS: Aquí se guardan los paquetes fuente RPM construidos.
  ```

3.  Ejecutar el comando rpmdev-newspec holaMundoRPM

  ```bash
  \$ rpmdev-newspec \~/rpmbuild/SPECS/holaMundoRPM
  ```

  Este comando crea el archivo holaMundoRPM.spec en el directorio \~/rpmbuild/SPECS/, el cual modificaremos según nuestras necesidades.

4.  Modificar el archivo \~/rpmbuild/SPECS/holaMundoRPM.spec con los datos de nuestra aplicación.
5.  Ejecutar el comando:

  ```bash
  \$ rpmbuild -ba \~/rpmbuild/SPECS/holaMundoRPM.spec
  ```

  Este comando realiza todo el proceso de creación del RPM.

## Conformación del guion del archivo holaMundoRPM.spec:

Este archivo hay que ubicarlo en \~/rpmbuild/SPECS.

**Name: holaMundoRPM :** El nombre contiene el nombre del paquete no
debé contener versión.

**Version: 1.0.0 :** La versión contiene la versión de la aplicación.

**Release: 1%{?dist} :** Release se refiere a la versión de \"release\"
del paquete y el marcador %{?dist} agrega automáticamente un sufijo de
distribución dependiendo de la plataforma en la que se esté construyendo
el paquete.

  **1:** Es el número de release de este paquete. Se incrementa cada vez
que haces cambios en el paquete pero no en la versión del software. Por
ejemplo, si lanzas varias versiones del paquete disableSS 0.1, podrías
incrementar este número a 2, 3, etc., cuando actualices el empaquetado o
ajustes menores.

  **%{?dist}:** Es un macro de RPM que inserta automáticamente una
etiqueta de distribución (por ejemplo, .fc38 en Fedora 38 o .el8 en
CentOS 8). Esto permite identificar rápidamente el sistema operativo o
distribución para el que fue construido el paquete. Si el macro %{?dist}
no está definido, simplemente no se añade nada.

**Summary: \... :** Resumen breve (\< 70 caracteres) del paquete.

**License: GPLv3 :** Resumen breve (\< 70 caracteres) de la licencia del
paquete. Por ejemplo: Licencia: GPLv3

**URL: https://\...:** URL que proporciona más información sobre el
paquete, normalmente un sitio web.

**Source0: %{name}-%{version}.tar.gz:** Archivo donde se encuentran las
fuentes del proyecto se construye con la información {Nombre} y
{Version} proporcionados anteriormente. este archivo deberá ser
construido con los archivos del proyecto dentro de un directorio con el
nombre del proyecto un guión y la versión, en el caso de holaMundoRPM la
versión es la 1.0.0 por lo que el archivo .tar.gz se puede construir
como sigue:

\$ tar -czvf \~/rpmbuild/SOURCES/holaMundoRPM-1.0.0.tar.gz
holaMundoRPM-1.0.0/

 - Donde holaMundo-1.0.0/ es el directorio que contiene los archivos del
proyecto.

 - El nombre del archivo .tar.gz debe incluir también el nombre y la
versión, en este caso holaMundoRPM-1.0.0.tar.gz.

 - Como se observa en la instrucción, al decirle a tar que construya el
comprimido, también se le instruye para que de una vez lo posicione en
su directorio correspondiente \~/rpmbuild/SOURCES

**BuildRequires: gcc:** Esta línea indica las dependencias necesarias
para compilar el paquete. En este caso solo necesita de gcc.

**Requires: glibc:** Esta línea indica las dependencias necesarias para
ejecutar el paquete. En el caso de holaMundoRPM solo requiere gibc.

**BuildArch: x86_64:** No es necesaria para este proyecto, incluido por
completitud. Especifica la arquitectura en la que se ejecutará el
paquete binario resultante. Normalmente se trata de una arquitectura de
CPU como sparc, i386. La cadena \'noarch\' está reservada para
especificar que el paquete binario resultante es independiente de la
plataforma. Los paquetes típicos independientes de la plataforma son los
paquetes html, perl, python, java y ps.

**%description: ** %description es texto en formato libre, pero hay dos
cosas a tener en cuenta. El **Programa... **primero se refiere al
reformateo. Las líneas que comienzan con espacios en blanco se
consideran \"preformateadas\" y se dejarán como están. Las líneas
adyacentes sin espacios en blanco iniciales se consideran un solo
párrafo y pueden estar sujetas a formato mediante glint u otra
herramienta RPM.

**%prep:** Esta directiva marca el inicio de la sección \"prepare\" en
el proceso de construcción **%setup -q **del RPM. Aquí se colocan los
comandos necesarios para preparar el entorno de compilación, como la
extracción del código fuente.

**%setup -q**, Este comando dentro de la sección %prep descomprime y
extrae el archivo de origen (Source0). La opción -q suprime la mayoría
de los mensajes de salida para hacer el proceso menos verboso.
Básicamente, este comando extrae el archivo fuente holaMundoRPM.tar.gz
en un directorio de trabajo temporal para que el sistema de compilación
pueda acceder a los archivos.

**%build:** Esta sección indica el inicio del proceso de construcción
del paquete.

**gcc \... -o %{name} %{name}.c** Todo lo que está dentro de esta
sección se utiliza para compilar el código fuente y generar el
ejecutable.

**%install: **En %install, el diseño de instalación del software

**mkdir -p \$RPM_BUILD_ROOT%{\_bindir} **se prepara creando la
estructura de directorio

**install -m 755 %{name} %{buildroot}%{\_bindir} **necesaria en un
directorio \"raíz de compilación\" inicialmente vacío y copiando el
software recién creado allí en los lugares apropiados. Básicamente se
crea una estructura de como quedará instalada la aplicación siendo
\$RPM_BUILD_ROOT (\~/rpmbuild/BUILDROOT) la raíz del sistema. El comando
install es similar a cp, pero con funcionalidades adicionales. En este
caso, lo que hace es copiar un archivo con permisos específicos. Si no
lo conoces, te recomiendo te familiarices con el: man install.

**%files: %files** especifica qué archivos se van a incluir en el
paquete RPM y

**%{\_bindir}/%{name} **dónde deben instalarse en el sistema cuando el
paquete se instale. Aquí

**%license docs/GPLv3.txt **incluyen otros documentos (%doc
docs/Readme.md), licencias (%licence docs/GPLv3.txt), paginas man
(%{\_mandir}/man1/disableSS.1\*), etc.

**%changelog:** La sección **%changelog** es el registro de cambios,
lleva un formato fijo

**Wed \... -- 1.0.0-1 **(en ingles), revisar el archivo
holaMundoRPM.spec. Esta información

**Release de holaMundoRPM **es estatica, no se deben usar macros,
rpmlint marca advertencia si se usan macros, aunque de todas formas
generá elos RPMs, la última línea es información generica del release.

## Construir el/los RPMs:

Ejecutar la siguiente orden:

rpmbuild -ba \~/rpmbuild/SPECS/holaMundoRPM.spec

Al finalizar, si no hubo errores, encontraremos los siguientes RPMS:

\~/rpmbuild/SRPMS/holaMundoRPM-1.0.0-1.mga9.src.rpm

\~/rpmbuild/RPMS/x86_64/holaMundoRPM-1.0.0-1.mga9.x86_64.rpm

## holaMundoRPM.spec: {#holamundorpm.spec}

El archivo holaMundoRPM.spec es un guion de construcción con una
optimización ligera/media con información de depuración. Esta es la
recomendación de compilación para la distribución RPM.

La instrucción de compilación es la siguiente:

gcc -O2 -g -fno-omit-frame-pointer -mtune=generic
-fstack-protector-strong -D_FORTIFY_SOURCE=2 -pie -fPIE -Wall -Werror
-Wl,\--as-needed -o %{name} %{name}.c

Las banderas activas son las siguientes:

- -O2: Esta opción aplica optimizaciones comunes sin aumentar demasiado
  el tiempo de compilación ni comprometer la depuración. Es la opción
  recomendada para compilaciones de distribución.
- -g: Incluye información básica de depuración en el binario, que luego
  puede separarse en archivos de depuración independientes.
- -fno-omit-frame-pointer: No omite el puntero de marco, lo que facilita
  la depuración y el análisis post-mortem (core dumps).
- -mtune=generic: Generar un código optimizado para una amplia gama de
  CPUs.
- -fstack-protector-strong: Añade protecciones contra desbordamiento de
  pila, mejorando la seguridad del programa.
- -D_FORTIFY_SOURCE=2: Activa algunas optimizaciones adicionales en
  funciones estándar de C para mejorar la seguridad. Es ampliamente
  usado en distribuciones Linux.
- -pie -fPIE: Para generar un ejecutable independiente de la posición,
  útil para mejorar la seguridad al usar Address Space Layout
  Randomization (ASLR).
- -Wall: Activa un conjunto de advertencias que pueden ayudar a
  identificar posibles errores o malas prácticas en el código.
- -Werror: Convierte todas las advertencias en errores. Esto significa
  que si el compilador encuentra algo que normalmente advertiría,
  fallará la compilación.
- -Wl,\--as-needed: Es una opción que se pasa al enlazador (ld) y le
  indica que solo incluya en el ejecutable las bibliotecas que realmente
  se utilizan, evitando dependencias innecesarias.

## holaMundoRPMNoDebug.spec: {#holamundorpmnodebug.spec}

El archivo holaMundoRPMNoDebug.spec es un guión de construcción con una
optimización para generar una versión de release, sin debug y optimizado
al máximo.

La instrucción de compilación es la siguiente:

gcc -Wall -Werror -Wl,\--as-needed -O3 -g0 -s -march=native -flto -o
%{name} %{name}.c

Las banderas activas son las siguientes:

- -Wall: Activa un conjunto de advertencias que pueden ayudar a
  identificar posibles errores o malas prácticas en el código.
- -Werror: Convierte todas las advertencias en errores. Esto significa
  que si el compilador encuentra algo que normalmente advertiría,
  fallará la compilación.
- -Wl,\--as-needed: Es una opción que se pasa al enlazador (ld) y le
  indica que solo incluya en el ejecutable las bibliotecas que realmente
  se utilizan, evitando dependencias innecesarias.
- -O3: Aplica la optimización más agresiva disponible en gcc, lo que
  mejora el rendimiento del programa.
- -g0: Elimina toda información de depuración.
- -s: Eliminar código no usado, quita símbolos de depuración y minimizar
  el tamaño del ejecutable, eliminando secciones innecesarias.
- -march=native: Compila el código optimizado para la arquitectura de la
  CPU donde se está ejecutando la compilación, esta opción hay que
  usarla con cuidado, ya que que puede causar problemas en otros
  sistemas, por haber optimizado para la arquitectura de la CPU donde se
  está ejecutando la compilación.
- -flto: Usa la optimización de tiempo de enlace (Link Time
  Optimization) para hacer una optimización global entre los módulos del
  programa.
- 

El archivo spec holaMundoRPMNoDebug.spec, este guión de construcción de
RPM incluye la directiva:

%global debug_package %{nil}

La cual le dice al sistema de construcción RPM que no cree el subpaquete
debuginfo, por lo que el ejecutable no deberá incluir información de
depuración, es útil cuando el release esta optimizado al máximo para
eficiencia en velocidad y tamaño, lo cual no incluye información de
depuración, el archivo holaMundoRPMNoDebug.spec esta optimizado al
máximo.

## []{#anchor-1}Requisitos:

- gcc

## Licencia

[]{#anchor-2}Este proyecto está licenciado bajo la **GPLv3** (GNU
General Public License, versión 3). Esto significa que:

1.  Puedes utilizar, modificar y distribuir este software siempre que lo
    hagas bajo los mismos términos de la **GPLv3**.
2.  Cualquier modificación que hagas al código fuente y distribuyas
    también debe ser publicada bajo la **GPLv3**.
3.  El código fuente completo debe estar disponible para cualquier
    usuario que reciba una copia del programa.

Puedes encontrar una copia completa en el archivo *GPLv3.txt* de este
repositorio o en <https://www.gnu.org/licenses/gpl-3.0.html>.

Víctor Emmanuel Rivero Alonzo

2024/10/09
