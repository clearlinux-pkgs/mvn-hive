#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-hive
Version  : 1
Release  : 1
URL      : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-cli/1.2.1.spark2/hive-cli-1.2.1.spark2.jar
Source0  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-cli/1.2.1.spark2/hive-cli-1.2.1.spark2.jar
Source1  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-beeline/1.2.1.spark2/hive-beeline-1.2.1.spark2.jar
Source2  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-beeline/1.2.1.spark2/hive-beeline-1.2.1.spark2.pom
Source3  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-cli/1.2.1.spark2/hive-cli-1.2.1.spark2.pom
Source4  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-exec/1.2.1.spark2/hive-exec-1.2.1.spark2.jar
Source5  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-exec/1.2.1.spark2/hive-exec-1.2.1.spark2.pom
Source6  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-jdbc/1.2.1.spark2/hive-jdbc-1.2.1.spark2.jar
Source7  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-jdbc/1.2.1.spark2/hive-jdbc-1.2.1.spark2.pom
Source8  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-metastore/1.2.1.spark2/hive-metastore-1.2.1.spark2.jar
Source9  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-metastore/1.2.1.spark2/hive-metastore-1.2.1.spark2.pom
Source10  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive/1.2.1.spark2/hive-1.2.1.spark2.pom
Source11  : https://repo1.maven.org/maven2/org/spark-project/hive/hive/1.2.1.spark2/hive-1.2.1.spark2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-hive-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-hive package.
Group: Data

%description data
data components for the mvn-hive package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-cli/1.2.1.spark2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-cli/1.2.1.spark2/hive-cli-1.2.1.spark2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-beeline/1.2.1.spark2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-beeline/1.2.1.spark2/hive-beeline-1.2.1.spark2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-beeline/1.2.1.spark2
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-beeline/1.2.1.spark2/hive-beeline-1.2.1.spark2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-cli/1.2.1.spark2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-cli/1.2.1.spark2/hive-cli-1.2.1.spark2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-exec/1.2.1.spark2
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-exec/1.2.1.spark2/hive-exec-1.2.1.spark2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-exec/1.2.1.spark2
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-exec/1.2.1.spark2/hive-exec-1.2.1.spark2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-jdbc/1.2.1.spark2
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-jdbc/1.2.1.spark2/hive-jdbc-1.2.1.spark2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-jdbc/1.2.1.spark2
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-jdbc/1.2.1.spark2/hive-jdbc-1.2.1.spark2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-metastore/1.2.1.spark2
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-metastore/1.2.1.spark2/hive-metastore-1.2.1.spark2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-metastore/1.2.1.spark2
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-metastore/1.2.1.spark2/hive-metastore-1.2.1.spark2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive/1.2.1.spark2
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive/1.2.1.spark2/hive-1.2.1.spark2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive/1.2.1.spark2
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive/1.2.1.spark2/hive-1.2.1.spark2.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/spark-project/hive/hive-beeline/1.2.1.spark2/hive-beeline-1.2.1.spark2.jar
/usr/share/java/.m2/repository/org/spark-project/hive/hive-beeline/1.2.1.spark2/hive-beeline-1.2.1.spark2.pom
/usr/share/java/.m2/repository/org/spark-project/hive/hive-cli/1.2.1.spark2/hive-cli-1.2.1.spark2.jar
/usr/share/java/.m2/repository/org/spark-project/hive/hive-cli/1.2.1.spark2/hive-cli-1.2.1.spark2.pom
/usr/share/java/.m2/repository/org/spark-project/hive/hive-exec/1.2.1.spark2/hive-exec-1.2.1.spark2.jar
/usr/share/java/.m2/repository/org/spark-project/hive/hive-exec/1.2.1.spark2/hive-exec-1.2.1.spark2.pom
/usr/share/java/.m2/repository/org/spark-project/hive/hive-jdbc/1.2.1.spark2/hive-jdbc-1.2.1.spark2.jar
/usr/share/java/.m2/repository/org/spark-project/hive/hive-jdbc/1.2.1.spark2/hive-jdbc-1.2.1.spark2.pom
/usr/share/java/.m2/repository/org/spark-project/hive/hive-metastore/1.2.1.spark2/hive-metastore-1.2.1.spark2.jar
/usr/share/java/.m2/repository/org/spark-project/hive/hive-metastore/1.2.1.spark2/hive-metastore-1.2.1.spark2.pom
/usr/share/java/.m2/repository/org/spark-project/hive/hive/1.2.1.spark2/hive-1.2.1.spark2.pom
