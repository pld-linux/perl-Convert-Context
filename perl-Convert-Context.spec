%define	pdir	Convert
%define	pnam	Context
%include	/usr/lib/rpm/macros.perl
Summary:	Perl Convert-Context module
Summary(pl):	Modu³ Perla Convert-Context
Name:		perl-Convert-Context
Version:	0.501
Release:	9

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert-Context allows you to access attributed strings similiar to
perl's normal strings.

%description -l pl
Convert-Context umo¿liwia dostêp do ³añcuchów z przyporz±dkowanymi
atrybutami w podobny sposób jak do normalnych ³añcuchów.

%prep
%setup -q -n Convert-Context-%{version}

%build
perl Makefile.PL

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Convert/Context.pm
%{_mandir}/man3/*
