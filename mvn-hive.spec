#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-hive
Version  : 1
Release  : 4
URL      : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-cli/1.2.1.spark2/hive-cli-1.2.1.spark2.jar
Source0  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-cli/1.2.1.spark2/hive-cli-1.2.1.spark2.jar
Source1  : https://repo.maven.apache.org/maven2/org/apache/hive/hcatalog/hcatalog-core/0.12.0/hcatalog-core-0.12.0.jar
Source2  : https://repo.maven.apache.org/maven2/org/apache/hive/hcatalog/hcatalog-core/0.12.0/hcatalog-core-0.12.0.pom
Source3  : https://repo.maven.apache.org/maven2/org/apache/hive/hcatalog/hcatalog/0.12.0/hcatalog-0.12.0.pom
Source4  : https://repo.maven.apache.org/maven2/org/apache/hive/hive-cli/0.12.0/hive-cli-0.12.0.jar
Source5  : https://repo.maven.apache.org/maven2/org/apache/hive/hive-cli/0.12.0/hive-cli-0.12.0.pom
Source6  : https://repo.maven.apache.org/maven2/org/apache/hive/hive-common/0.12.0/hive-common-0.12.0.jar
Source7  : https://repo.maven.apache.org/maven2/org/apache/hive/hive-common/0.12.0/hive-common-0.12.0.pom
Source8  : https://repo.maven.apache.org/maven2/org/apache/hive/hive-exec/0.12.0/hive-exec-0.12.0.jar
Source9  : https://repo.maven.apache.org/maven2/org/apache/hive/hive-exec/0.12.0/hive-exec-0.12.0.pom
Source10  : https://repo.maven.apache.org/maven2/org/apache/hive/hive-metastore/0.12.0/hive-metastore-0.12.0.jar
Source11  : https://repo.maven.apache.org/maven2/org/apache/hive/hive-metastore/0.12.0/hive-metastore-0.12.0.pom
Source12  : https://repo.maven.apache.org/maven2/org/apache/hive/hive-serde/0.12.0/hive-serde-0.12.0.jar
Source13  : https://repo.maven.apache.org/maven2/org/apache/hive/hive-serde/0.12.0/hive-serde-0.12.0.pom
Source14  : https://repo.maven.apache.org/maven2/org/apache/hive/hive-service/0.12.0/hive-service-0.12.0.jar
Source15  : https://repo.maven.apache.org/maven2/org/apache/hive/hive-service/0.12.0/hive-service-0.12.0.pom
Source16  : https://repo.maven.apache.org/maven2/org/apache/hive/hive-shims/0.12.0/hive-shims-0.12.0.jar
Source17  : https://repo.maven.apache.org/maven2/org/apache/hive/hive-shims/0.12.0/hive-shims-0.12.0.pom
Source18  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-beeline/1.2.1.spark2/hive-beeline-1.2.1.spark2.jar
Source19  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-beeline/1.2.1.spark2/hive-beeline-1.2.1.spark2.pom
Source20  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-cli/1.2.1.spark2/hive-cli-1.2.1.spark2.pom
Source21  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-exec/1.2.1.spark2/hive-exec-1.2.1.spark2.jar
Source22  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-exec/1.2.1.spark2/hive-exec-1.2.1.spark2.pom
Source23  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-jdbc/1.2.1.spark2/hive-jdbc-1.2.1.spark2.jar
Source24  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-jdbc/1.2.1.spark2/hive-jdbc-1.2.1.spark2.pom
Source25  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-metastore/1.2.1.spark2/hive-metastore-1.2.1.spark2.jar
Source26  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive-metastore/1.2.1.spark2/hive-metastore-1.2.1.spark2.pom
Source27  : https://repo.maven.apache.org/maven2/org/spark-project/hive/hive/1.2.1.spark2/hive-1.2.1.spark2.pom
Source28  : https://repo1.maven.org/maven2/org/apache/hive/hive-storage-api/2.2.1/hive-storage-api-2.2.1.jar
Source29  : https://repo1.maven.org/maven2/org/apache/hive/hive-storage-api/2.2.1/hive-storage-api-2.2.1.pom
Source30  : https://repo1.maven.org/maven2/org/spark-project/hive/hive/1.2.1.spark2/hive-1.2.1.spark2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-hive-data = %{version}-%{release}
Requires: mvn-hive-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
No detailed description available

%package data
Summary: data components for the mvn-hive package.
Group: Data

%description data
data components for the mvn-hive package.


%package license
Summary: license components for the mvn-hive package.
Group: Default

%description license
license components for the mvn-hive package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-hive
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-hive/LICENSE
cp NOTICE %{buildroot}/usr/share/package-licenses/mvn-hive/NOTICE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-cli/1.2.1.spark2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-cli/1.2.1.spark2/hive-cli-1.2.1.spark2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hcatalog/hcatalog-core/0.12.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hcatalog/hcatalog-core/0.12.0/hcatalog-core-0.12.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hcatalog/hcatalog-core/0.12.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hcatalog/hcatalog-core/0.12.0/hcatalog-core-0.12.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hcatalog/hcatalog/0.12.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hcatalog/hcatalog/0.12.0/hcatalog-0.12.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-cli/0.12.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-cli/0.12.0/hive-cli-0.12.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-cli/0.12.0
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-cli/0.12.0/hive-cli-0.12.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-common/0.12.0
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-common/0.12.0/hive-common-0.12.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-common/0.12.0
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-common/0.12.0/hive-common-0.12.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-exec/0.12.0
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-exec/0.12.0/hive-exec-0.12.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-exec/0.12.0
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-exec/0.12.0/hive-exec-0.12.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-metastore/0.12.0
cp %{SOURCE10} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-metastore/0.12.0/hive-metastore-0.12.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-metastore/0.12.0
cp %{SOURCE11} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-metastore/0.12.0/hive-metastore-0.12.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-serde/0.12.0
cp %{SOURCE12} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-serde/0.12.0/hive-serde-0.12.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-serde/0.12.0
cp %{SOURCE13} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-serde/0.12.0/hive-serde-0.12.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-service/0.12.0
cp %{SOURCE14} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-service/0.12.0/hive-service-0.12.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-service/0.12.0
cp %{SOURCE15} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-service/0.12.0/hive-service-0.12.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-shims/0.12.0
cp %{SOURCE16} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-shims/0.12.0/hive-shims-0.12.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-shims/0.12.0
cp %{SOURCE17} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-shims/0.12.0/hive-shims-0.12.0.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-beeline/1.2.1.spark2
cp %{SOURCE18} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-beeline/1.2.1.spark2/hive-beeline-1.2.1.spark2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-beeline/1.2.1.spark2
cp %{SOURCE19} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-beeline/1.2.1.spark2/hive-beeline-1.2.1.spark2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-cli/1.2.1.spark2
cp %{SOURCE20} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-cli/1.2.1.spark2/hive-cli-1.2.1.spark2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-exec/1.2.1.spark2
cp %{SOURCE21} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-exec/1.2.1.spark2/hive-exec-1.2.1.spark2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-exec/1.2.1.spark2
cp %{SOURCE22} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-exec/1.2.1.spark2/hive-exec-1.2.1.spark2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-jdbc/1.2.1.spark2
cp %{SOURCE23} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-jdbc/1.2.1.spark2/hive-jdbc-1.2.1.spark2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-jdbc/1.2.1.spark2
cp %{SOURCE24} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-jdbc/1.2.1.spark2/hive-jdbc-1.2.1.spark2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-metastore/1.2.1.spark2
cp %{SOURCE25} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-metastore/1.2.1.spark2/hive-metastore-1.2.1.spark2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-metastore/1.2.1.spark2
cp %{SOURCE26} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive-metastore/1.2.1.spark2/hive-metastore-1.2.1.spark2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive/1.2.1.spark2
cp %{SOURCE27} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive/1.2.1.spark2/hive-1.2.1.spark2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-storage-api/2.2.1
cp %{SOURCE28} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-storage-api/2.2.1/hive-storage-api-2.2.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-storage-api/2.2.1
cp %{SOURCE29} %{buildroot}/usr/share/java/.m2/repository/org/apache/hive/hive-storage-api/2.2.1/hive-storage-api-2.2.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive/1.2.1.spark2
cp %{SOURCE30} %{buildroot}/usr/share/java/.m2/repository/org/spark-project/hive/hive/1.2.1.spark2/hive-1.2.1.spark2.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/hive/hcatalog/hcatalog-core/0.12.0/hcatalog-core-0.12.0.jar
/usr/share/java/.m2/repository/org/apache/hive/hcatalog/hcatalog-core/0.12.0/hcatalog-core-0.12.0.pom
/usr/share/java/.m2/repository/org/apache/hive/hcatalog/hcatalog/0.12.0/hcatalog-0.12.0.pom
/usr/share/java/.m2/repository/org/apache/hive/hive-cli/0.12.0/hive-cli-0.12.0.jar
/usr/share/java/.m2/repository/org/apache/hive/hive-cli/0.12.0/hive-cli-0.12.0.pom
/usr/share/java/.m2/repository/org/apache/hive/hive-common/0.12.0/hive-common-0.12.0.jar
/usr/share/java/.m2/repository/org/apache/hive/hive-common/0.12.0/hive-common-0.12.0.pom
/usr/share/java/.m2/repository/org/apache/hive/hive-exec/0.12.0/hive-exec-0.12.0.jar
/usr/share/java/.m2/repository/org/apache/hive/hive-exec/0.12.0/hive-exec-0.12.0.pom
/usr/share/java/.m2/repository/org/apache/hive/hive-metastore/0.12.0/hive-metastore-0.12.0.jar
/usr/share/java/.m2/repository/org/apache/hive/hive-metastore/0.12.0/hive-metastore-0.12.0.pom
/usr/share/java/.m2/repository/org/apache/hive/hive-serde/0.12.0/hive-serde-0.12.0.jar
/usr/share/java/.m2/repository/org/apache/hive/hive-serde/0.12.0/hive-serde-0.12.0.pom
/usr/share/java/.m2/repository/org/apache/hive/hive-service/0.12.0/hive-service-0.12.0.jar
/usr/share/java/.m2/repository/org/apache/hive/hive-service/0.12.0/hive-service-0.12.0.pom
/usr/share/java/.m2/repository/org/apache/hive/hive-shims/0.12.0/hive-shims-0.12.0.jar
/usr/share/java/.m2/repository/org/apache/hive/hive-shims/0.12.0/hive-shims-0.12.0.pom
/usr/share/java/.m2/repository/org/apache/hive/hive-storage-api/2.2.1/hive-storage-api-2.2.1.jar
/usr/share/java/.m2/repository/org/apache/hive/hive-storage-api/2.2.1/hive-storage-api-2.2.1.pom
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-hive/LICENSE
/usr/share/package-licenses/mvn-hive/NOTICE
