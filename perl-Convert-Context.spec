%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	Context
Summary:	Convert::Context Perl module - an attributed text data type
Summary(pl):	Modu³ Perla Convert::Context - typ danych: tekst z atrybutami
Name:		perl-Convert-Context
Version:	0.501
Release:	11
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	701f73725e44b34f89a0cba23e74d672
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::Context module maintains attributed strings.  It allows you
to access those strings similiar to Perl's normal strings.

%description -l pl
Modu³ Convert::Context zarz±dza ³añcuchami tekstowymi z
przyporz±dkowanymi atrybutami. Umo¿liwia dostêp do tych ³añcuchów w
podobny sposób jak do normalnych ³añcuchów Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Convert/Context.pm
%{_mandir}/man3/*
