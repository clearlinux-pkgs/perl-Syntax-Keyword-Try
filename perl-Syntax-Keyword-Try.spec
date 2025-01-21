#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v18
# autospec commit: eaa4f711da30
#
Name     : perl-Syntax-Keyword-Try
Version  : 0.30
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Syntax-Keyword-Try-0.30.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Syntax-Keyword-Try-0.30.tar.gz
Summary  : 'a C<try/catch/finally> syntax for perl'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Syntax-Keyword-Try-license = %{version}-%{release}
Requires: perl-Syntax-Keyword-Try-perl = %{version}-%{release}
Requires: perl(XS::Parse::Keyword)
BuildRequires : buildreq-cpan
BuildRequires : perl(File::ShareDir)
BuildRequires : perl(XS::Parse::Keyword::Builder)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Syntax::Keyword::Try - a try/catch/finally syntax for perl
SYNOPSIS
use Syntax::Keyword::Try;

sub foo {
try {
attempt_a_thing();
return "success";
}
catch ($e) {
warn "It failed - $e";
return "failure";
}
}

%package dev
Summary: dev components for the perl-Syntax-Keyword-Try package.
Group: Development
Provides: perl-Syntax-Keyword-Try-devel = %{version}-%{release}
Requires: perl-Syntax-Keyword-Try = %{version}-%{release}

%description dev
dev components for the perl-Syntax-Keyword-Try package.


%package license
Summary: license components for the perl-Syntax-Keyword-Try package.
Group: Default

%description license
license components for the perl-Syntax-Keyword-Try package.


%package perl
Summary: perl components for the perl-Syntax-Keyword-Try package.
Group: Default
Requires: perl-Syntax-Keyword-Try = %{version}-%{release}

%description perl
perl components for the perl-Syntax-Keyword-Try package.


%prep
%setup -q -n Syntax-Keyword-Try-0.30
cd %{_builddir}/Syntax-Keyword-Try-0.30

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Syntax-Keyword-Try
cp %{_builddir}/Syntax-Keyword-Try-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Syntax-Keyword-Try/ff3cb0dfd45f53bab83fc8e6480335b7afdc4bbe || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Syntax::Keyword::Try.3
/usr/share/man/man3/Syntax::Keyword::Try::Deparse.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Syntax-Keyword-Try/ff3cb0dfd45f53bab83fc8e6480335b7afdc4bbe

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
